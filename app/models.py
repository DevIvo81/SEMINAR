from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    picture = db.Column(db.String(300), nullable=False, default='default.jpg')
    favorite_plant = db.Column(db.String(120))
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    
    def __repr__(self):
        return f"<User {self.name}>"



class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(300), nullable=False, default='Plant name')
    photo = db.Column(db.String(300), nullable=False, default='tenica.png')

    temperature = db.Column(db.Integer, nullable=False, default=10)
    pH_F = db.Column(db.Integer, nullable=False, default=7)
    humidity = db.Column(db.Integer, nullable=False, default=44)
    
    def __repr__(self):
        return f"<Plant('id={self.id}', 'name={self.name}', 'photo={self.photo}')>"
    
    

class Jar(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, default='Posuda') 
        
    plant_name = db.Column(db.String(50), default='Nema biljke')
    photo = db.Column(db.String(300), nullable=False, default='default.jpg')
    
    temperature = db.Column(db.Integer, nullable=False, default=10)
    pH_F = db.Column(db.Integer, nullable=False, default=7)
    humidity = db.Column(db.Integer, nullable=False, default=44)
    



