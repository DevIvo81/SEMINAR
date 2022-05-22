from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError

from .models import User


#region USERS 
class RegistrationForm(FlaskForm):   
    name = StringField('Vaše ime', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Vaša lozinka', validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField('Ponovite lozinku', 
                                    validators=[DataRequired(), EqualTo('password'), Length(min=4, max=20)])
    submit = SubmitField('Registriraj se')
    
    def validate_name(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('Postoji korisnik pod tim imenom!')

class LoginForm(FlaskForm):
    name = StringField('Vaše ime', validators=[DataRequired()])
    password = PasswordField('Vaša lozinka', validators=[DataRequired()])
    submit = SubmitField('Ulogiraj se')    

#endregion USERS


#region PLANTS AND JARS

class NewPlantForm(FlaskForm):
    
    name = StringField('Upišite ime biljke', validators=[DataRequired()])
    photo = FileField('Dodajte fotografiju', 
                        validators=[FileRequired(), 
                                    FileAllowed(['jpg', 'png', 'svg', 'gif', 'bmp'], message="File ext not allowed!")])
    details = TextAreaField('Tekst o biljci', 
                            validators=[DataRequired()])
    temperature = IntegerField('Upiši najnižu temperaturu za biljku', validators=[DataRequired()])
    phf = IntegerField('Upiši najnižu pH vijednost za biljku', validators=[DataRequired()])
    humidity = IntegerField('Upiši potrebni postotak vlage za biljku', validators=[DataRequired()])
    
    submit = SubmitField('Add New Plant')

class AddPlantForm(FlaskForm):  
    biljka = IntegerField('Upiši id biljke', validators=[DataRequired()])
    submit = SubmitField('Add New Plant')

class AddJarForm(FlaskForm):
    name = StringField('Upišite lokaciju posude', validators=[DataRequired()])
    submit = SubmitField('Add New Jar')

class DeleteJarForm(FlaskForm):
    submit = SubmitField('Delete')

#endregion PLANTS AND JARS   
