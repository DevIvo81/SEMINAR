from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class NamerForm(FlaskForm):
    name = StringField('Upišite vaše ime', validators=[DataRequired()])
    submit = SubmitField('Dodaj ime')

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Add Profile Picture', validators=[FileAllowed(['jpg', 'png', 'svg'])])
    favorite_plant = StringField('Favorite Plant', validators=[DataRequired()])
    
    submit = SubmitField('Dodaj korisnika')

# TODO - JAR UPDATE FORM
class JarUpdateForm(FlaskForm):
    pass