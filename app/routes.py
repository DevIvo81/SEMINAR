import json
from datetime import datetime
from random import choice
from flask import render_template, flash, url_for, redirect, request, jsonify

from . import app, db
from .forms import RegistrationForm, LoginForm, AddPlantForm, AddJarForm, DeleteJarForm
from .models import User, Jar, Plant
from . import get_all_readings


#region USER ROUTES

@app.route('/', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        
        user = User.query.filter_by(name=form.name.data).first()
        
        if user:
            if user.name == form.name.data and user.password == form.password.data:
                flash(f'Loginacija uspješna!', category='success')
                return redirect(url_for('jars'))
            else:
                flash('Pogrešno ime ili lozinka, pokušajte ponovno!', category='danger')
        else:
            flash('Nepostojeći korisnik, pokušajte ponovno!', category='danger')
            
    return render_template('home/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user:
            flash(f'Greška, korisnik pod imenom {user.name} već postoji. Odaberite drugo ime!!', category='danger')
        else:
            user = User(
                name=form.name.data, 
                password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash(f'Registracija uspješna, korisnik {user.name} dodan u bazu!!', category='success')
        form.name.data = ''
        form.password.data = ''
        form.confirm_password.data = ''
    
    return render_template('home/register.html', form=form)



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
    
    form = AddJarForm()
    
    one_jar = Jar()
    
    if form.validate_on_submit():
        one_jar.name = form.name.data
        form.name.data = ''
        db.session.add(one_jar)
        db.session.commit()
        flash('Posuda dodana!', category='success')

    jars = Jar.query.order_by(Jar.id)
    
    return render_template('jars/jars.html',
                        jars=jars,
                        form=form)


@app.route('/jar_details/<int:jar_id>')
def jar_details(jar_id):
    
    jar = Jar.query.get(jar_id)
    plant = Plant.query.filter_by(name=jar.plant_name).first()
    
    return render_template('jars/jar_details.html',
                            jar = jar,
                            plant = plant)
    

@app.route('/jar_to_delete/<int:jar_id>')
def jar_to_delete(jar_id):
    
    jar = Jar.query.get(jar_id)
    plant = Plant.query.filter_by(name=jar.plant_name).first()
    
    return render_template('jars/jar_to_delete.html',
                            jar = jar,
                            plant = plant)


@app.route('/jar/delete/<int:jar_id>', methods=['GET', 'POST'])
def delete_jar(jar_id):
    
    jar = Jar.query.get(jar_id)
    
    db.session.delete(jar)
    db.session.commit()
    flash('Posuda uklonjena!', category='danger')
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
        flash('Biljka dodana!', category='success')
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
    flash('Posuda ispražnjena!', category='danger')
    return redirect(url_for('jar_details', jar_id=jar.id))


@app.route('/jars/sync/')
def sync():
    
    jars = Jar.query.order_by(Jar.id)
    
    for jar in jars:
        readings = get_all_readings()
        jar.temperature = readings[0]
        jar.phf = readings[1]
        jar.humidity = readings[2]
        
        db.session.commit()
    
    return redirect(url_for('jars'))

@app.route('/jar/sync/<int:jar_id>', methods=['GET', 'POST'])
def sync_jar(jar_id):
    
    jar = Jar.query.get(jar_id)
    
    readings = get_all_readings()
    
    jar.temperature = readings[0]
    jar.phf = readings[1]
    jar.humidity = readings[2]
    
    db.session.commit()
    
    return redirect(url_for('jar_details', jar_id=jar.id))

@app.route('/plants/api')
def plants_api():
    
    json_list = []
    
    pls = Plant.query.order_by(Plant.id)
    
    for p in pls:
        json_list.append(p.to_dict())
    
    return jsonify(json_list)

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