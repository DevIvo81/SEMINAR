from datetime import datetime
from random import choice
from flask import render_template, flash, url_for, redirect, request

from . import app, db
from .forms import NamerForm, UserForm, AddPlantForm
from .models import User, Jar, Plant
from . import get_all_readings

#region USER ROUTES

@app.route('/')
def index():
    first_name = "Ivo"
    current_date = datetime.utcnow()
    stuff = "This is bold text"
    
    flash('Dobrodošli na PyFlora stranicu!', category='info')
    
    favorite_pizza =     ['Šunka', 'Sir', 'Gljive', 41]
    return render_template('home/index.html',
                        first_name=first_name,
                        stuff=stuff,
                        favorite_pizza=favorite_pizza,
                        current_date=current_date)

@app.route('/user/<name>')
def user(name):
    return render_template('users/user.html',
                            user_name=name)


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data #... Take submitted text and store it to 'name'
        form.name.data = '' # ... Reset text in form cell
        flash(f'Bravo {name.capitalize()}... Forma uspješno ispunjena!', category='success')
        
    return render_template('users/name.html',
                        name=name,
                        form=form)

@app.route('/user/add', methods=['POST', 'GET'])
def add_user():
    name = None
    form = UserForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(name=form.name.data, email=form.email.data, favorite_plant=form.favorite_plant.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        form.favorite_plant.data = ''
        flash(f'Korisnik { user.name } uspješno dodan!', category='success')
    
    all_users = User.query.all()
    return render_template('users/add_user.html',
                            form=form,
                            name=name,
                            all_users=all_users)

# # Update database record - id is passed to function
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     #? ... taking form for user to be updated
#     form = UserForm()
#     #? ... Query User by id
#     name_to_update = User.query.get_or_404(id)
#     # ... checking if anything was posted by user
#     if request.method == 'POST':
#         name_to_update.name = request.form['name']
#         name_to_update.email = request.form['email']
#         try:
#             db.session.commit()
#             flash('Ažuriranje uspješno!', category='success')
#             return render_template('users/update.html',
#                                 form=form,
#                                 name_to_update=name_to_update)
#         except:
#             flash('Nešto ne štima...!', category='danger')
#             return render_template('users/update.html',
#                                 form=form,
#                                 name_to_update=name_to_update)
#     else:
#         return render_template('users/update.html',
#                                 form=form,
#                                 name_to_update=name_to_update)
        
# TODO: TRY TO MAKE UPDATE FUNCTION WITH if form.validate_on_submit():
#? DONE!

# Update database record - id is passed to function
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    #? ... taking form for user to be updated
    form = UserForm()
    #? ... Query User by id
    name_to_update = User.query.get_or_404(id)
    if form.validate_on_submit():
        name_to_update.name = form.name.data
        name_to_update.email = form.email.data
        name_to_update.favorite_plant = form.favorite_plant.data
        try:
            db.session.commit()
            flash('Ažuriranje uspješno!', category='success')
            return render_template('users/update.html',
                                form=form,
                                name_to_update=name_to_update)
        except:
            flash('Nešto ne štima...!', category='danger')
            return render_template('users/update.html',
                                form=form,
                                name_to_update=name_to_update)
    else:
        return render_template('users/update.html',
                                form=form,
                                name_to_update=name_to_update)

#endregion USER ROUTES


#region PLANTS AND JARS

@app.route('/plants')
def plants():
    plants = Plant.query.order_by(Plant.id)
        
    return render_template('plants/plants.html',
                            plants=plants)
    

@app.route('/plant_details/<int:plant_id>/<string:plant_name>')
def plant_details(plant_id, plant_name):
    plant = Plant.query.get(plant_id)
    return render_template('plants/plant_details.html',
                            plant = plant)


@app.route('/jars', methods=['GET', 'POST'])
def jars():
    
    jars = Jar.query.order_by(Jar.id)
    
    for jar in jars:
        plant = Jar.query.get(jar.id)
    
    return render_template('jars/jars.html',
                        jars = jars,
                        plant=plant)


@app.route('/jar_details/<int:jar_id>')
def jar_details(jar_id):
    
    jar = Jar.query.get(jar_id)
    plant = Plant.query.filter_by(name=jar.plant_name).first()
    
    return render_template('jars/jar_details.html',
                            jar = jar,
                            plant = plant)


@app.route('/jar/add', methods=['GET', 'POST'])
def add_jar():
    
    jar = Jar()
    
    db.session.add(jar)
    db.session.commit()
    
    return redirect(url_for('jars'))


@app.route('/jar/delete/<int:jar_id>', methods=['GET', 'POST'])
def delete_jar(jar_id):
    
    jar = Jar.query.get(jar_id)
    
    db.session.delete(jar)
    db.session.commit()
    
    return redirect(url_for('jars'))


@app.route('/jar/add_plant/<int:jar_id>', methods=['GET', 'POST'])
def add_plant(jar_id):
    
    form = AddPlantForm()
    
    if form.validate_on_submit():
        # ... Fetching data
        jar = Jar.query.get(jar_id)
        plant = Plant.query.get(form.biljka.data)
        
        # ... Updating data
        jar.plant_name = plant.name
        jar.photo = plant.photo
        
        db.session.commit()
        return redirect(url_for('jar_details', jar_id=jar.id))

    all_plants = Plant.query.all()
    
    return render_template('jars/add_plant.html',
                        form=form,
                        all_plants=all_plants)


@app.route('/jar/empty/<int:jar_id>', methods=['GET', 'POST'])
def empty_jar(jar_id):
    
    jar = Jar.query.get(jar_id)
    jar.plant_name = 'Plantless'
    jar.photo = 'default.jpg'
    
    db.session.commit()
    
    return redirect(url_for('jar_details', jar_id=jar.id))


@app.route('/jars/sync/', methods=['GET', 'POST'])
def sync():
    
    jars = Jar.query.order_by(Jar.id)
    
    for jar in jars:
        readings = get_all_readings()
        jar.temperature = readings[0]
        jar.pH_F = readings[1]
        jar.humidity = readings[2]
        
        db.session.commit()
    
    return redirect(url_for('jars'))





#endregion PLANTS AND JARS


#region CUSTOM ERROR PAGES

# 404
@app.errorhandler(404)
def page_not_found(err):
        return render_template('err/404.html'), 404
    
# 500
@app.errorhandler(500)
def page_not_found(err):
        return render_template('err/500.html'), 500
#endregion CUSTOM ERROR PAGES