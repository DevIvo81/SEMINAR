from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email, Length


#region USERS 
class RegistrationForm(FlaskForm):   
    name = StringField('Vaše ime', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Vaša lozinka', validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField('Ponovite lozinku', 
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registriraj se')    


class LoginForm(FlaskForm):
    name = StringField('Vaše ime', validators=[DataRequired()])
    password = PasswordField('Vaša lozinka', validators=[DataRequired()])
    submit = SubmitField('Ulogiraj se')    

#endregion USERS


#region PLANTS AND JARS
class AddPlantForm(FlaskForm):  
    biljka = IntegerField('Upiši id biljke', validators=[DataRequired()])
    submit = SubmitField('Add New Plant')

class AddJarForm(FlaskForm):
    name = StringField('Upišite lokaciju posude', validators=[DataRequired()])
    submit = SubmitField('Add New Jar')

#endregion PLANTS AND JARS   
