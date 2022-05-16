from datetime import datetime
from random import choice
from flask import render_template, flash, url_for, redirect, request
from . import app, db
from .forms import NamerForm, UserForm
from .models import User, Jar, Plant

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
            user = User(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash(f'Korisnik { user.name } uspješno dodan!', category='success')
    
    all_users = User.query.all()
    return render_template('users/add_user.html',
                            form=form,
                            all_users=all_users)

# Update database record - id is passed to function
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    #? ... taking form for user to be updated
    form = UserForm()
    #? ... Query User by id
    name_to_update = User.query.get_or_404(id)
    # ... checking if anything was posted by user
    if request.method == 'POST':
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
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
        
# TODO: TRY TO MAKE UPDATE FUNCTION WITH if form.validate_on_submit():

#endregion USER ROUTES


#region PLANTS AND JARS

@app.route('/plants')
def plants():
    plants = Plant.query.order_by(Plant.id)
        
    return render_template('plants/plants.html',
                            plants=plants)
    

@app.route('/plant_details/<int:plant_id>')
def plant_details(plant_id):
    plant = Plant.query.get(plant_id)
    return render_template('plants/plant_details.html',
                            plant = plant)


@app.route('/jars')
def jars():
    temperature = [x/10 for x in range(120, 355, 5)]
    temp = choice(temperature)
    
    humidities = [x/10 for x in range(30, 100)]
    hum = choice(humidities)
    
    jars = Jar.query.order_by(Jar.id)
        
    return render_template('jars/jars.html',
                            jars=jars,
                            temp = temp,
                            hum=hum)

@app.route('/jar_details/<int:jar_id>')
def jar_details(jar_id):
    jar = Jar.query.get(jar_id)
    return render_template('jars/jar_details.html',
                            jar = jar)

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
