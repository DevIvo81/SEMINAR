from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f"<User {self.name}>"


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(300), nullable=False, default='Plantless')
    photo = db.Column(db.String(300), nullable=False, default='default.jpg')

    temperature = db.Column(db.Integer, nullable=False, default=10)
    phf = db.Column(db.Integer, nullable=False, default=7)
    humidity = db.Column(db.Integer, nullable=False, default=44)
    
    def __repr__(self):
        return f"<Plant('id={self.id}', 'name={self.name}', 'photo={self.photo}')>"
    
    

class Jar(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False, default='Lokacija') 
        
    plant_name = db.Column(db.String(300), nullable=False, default='Plantless')
    photo = db.Column(db.String(300), nullable=False, default='default.jpg')
    
    temperature = db.Column(db.Integer, nullable=False, default=10)
    phf = db.Column(db.Integer, nullable=False, default=7)
    humidity = db.Column(db.Integer, nullable=False, default=44)
    



