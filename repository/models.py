import hello
from hello import *

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/DATA.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Biljke(db.Model):
    __tablename__ = 'biljke'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(150), nullable=False, unique=True)
    photo = db.Column(db.String(150), nullable=False, unique=True)
    


plants_list = [
    {
        'id' : 1,
        'name' : 'Bosiljak',
        'photo' : '01-bosiljak1-300x300.jpg',

    },
    {
        'id' : 2,
        'name' : 'Korijander',
        'photo' : '02-korijandar2-300x300.jpg',

    },
    {
        'id' : 3,
        'name' : 'Vlasac',
        'photo' : '03-luk-vlasac-300x300.jpg',
    },
    {
        'id' : 4,
        'name' : 'Mažuran',
        'photo' : '04-mazuran1-300x300',
    }
]

for plant in plants_list:
    db.session.add(plant)
    db.session.commit()