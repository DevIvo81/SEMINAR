from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import  DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#region CONFIGS
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/Podaci.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mojsupertajnikljuc'

db = SQLAlchemy(app)

#endregion CONFIGS


#region MODELS

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    
    ime = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Name {self.ime}>"

class Tegla(db.Model):
    __tablename__ = 'tegle'
    id = db.Column(db.Integer, primary_key=True)
    
    lokacija = db.Column(db.String(100), nullable=False)
    svjetlost = db.Column(db.String(100), nullable=False)
    vlaznost = db.Column(db.Float)
    pH = db.Column(db.Float)
    
    
class Biljka(db.Model):
    __tablename__ = 'biljke'
    id = db.Column(db.Integer, primary_key=True)
    
    ime = db.Column(db.String(300), nullable=False)
    photo = db.Column(db.String(300), nullable=False)
    
    svjetlost = db.Column(db.String(100), nullable=False)
    
    
    
    
    
#endregion MODELS


#region FORMS

class NamerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Registriraj')


class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Registriraj')
    
#endregion FORMS


#region ROUTES



@app.route('/')
def index():
    first_name = "Ivo"
    stuff = "This is bold text"
    
    flash('Dobrodošli na PyFlora stranicu!', category='warning')
    
    favorite_pizza = ['Šunka', 'Sir', 'Gljive', 41]
    return render_template('index.html',
                        first_name=first_name,
                        stuff=stuff,
                        favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',
                            user_name=name)


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Uspješno ispunjeno!', category='success')
        
    return render_template('name.html',
                        name=name,
                        form=form)


@app.route('/user/add', methods=['POST', 'GET'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(ime=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        ime = form.name.data
        
    return render_template('add_user.html',
                            form=form)

#endregion ROUTES



#region CUSTOM ERROR PAGES

# 404
@app.errorhandler(404)
def page_not_found(err):
        return render_template('404.html'), 404
    
# 500
@app.errorhandler(500)
def page_not_found(err):
        return render_template('500.html'), 500
#endregion CUSTOM ERROR PAGES

if __name__ == '__main__':
    app.run(debug=True)