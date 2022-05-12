from hello import app
from flask import session

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config[]

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Biljke(db.Model):
    __tablename__ = 'biljke'
    id = db.Column(db.Integer, primary_key=True)
    
    ime = db.Column(db.String(150), nullable=False, unique=True)
    slika = db.Column(db.String(150), nullable=False, unique=True)
    
