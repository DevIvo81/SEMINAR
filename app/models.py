from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    picture = db.Column(db.String(300), nullable=False, default='default.jpg')
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User {self.name}>"

class Jar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    biljka = db.Column(db.String(50), nullable=False, default='Prazna posuda')
    photo = db.Column(db.String(100), nullable=False, default='default.jpg')
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(300), nullable=False)
    photo = db.Column(db.String(300), nullable=False, default='default.png')
    
    def __repr__(self):
        return f"<Plant('id={self.id}', 'name={self.name}', 'photo={self.photo}')>"



