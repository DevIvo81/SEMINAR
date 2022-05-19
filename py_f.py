class User(db.Model):
    __tablename__ = 'biljka'
    id = db.Column(db.Integer, db.ForeignKey)
    name = db.Column(db.String, db.ForeignKey)
    password = db.Column(db.String, db.ForeignKey)


class Biljka(db.Model):
    __tablename__ = 'biljka'
    id = db.Column(db.Integer)
    
    naziv = db.Column(db.String)
    foto = db.Column(db.String) # ... putanja do slike
    
    posude = db.relationship('Posuda', backref=('biljka'), lazy=True)
    

class Posuda(db.Model):
    __tablename__ = 'posuda'
    id = db.Column(db.Integer, db.ForeignKey)
    
    naziv = db.Column(db.String, db.ForeignKey)
    
    # ...ForeignKey mora biti isti tip podatka na koji se veže
    biljka_id = db.Column(db.Integer, db.ForeignKey('biljka.id'))
    
    
'''
Jedna funkcija dohvaća sve posude


onda za svaku posudu bira iz popisa

'''

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
