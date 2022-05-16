from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class NamerForm(FlaskForm):
    name = StringField('Upišite vaše ime', validators=[DataRequired()])
    submit = SubmitField('Dodaj ime')

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Add Profile Picture', validators=[FileAllowed(['jpg', 'png', 'svg'])])
    submit = SubmitField('Dodaj korisnika')
    