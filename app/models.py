from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Name {self.name}>"

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



# db.create_all()

jars_list = [
    {
        'biljka' : 'Prazna posuda 1',
        'photo' : 'default.jpg'
    },
    {
        'biljka' : 'Prazna posuda 2',
        'photo' : 'default.jpg'
    },
    {
        'biljka' : 'Prazna posuda 3',
        'photo' : 'default.jpg'
    }
]





plants_list = [
    {
        'name' : 'Bosiljak',
        'photo' : '01-bosiljak1-300x300.jpg'

    },
    {
        'name' : 'Korijander',
        'photo' : '02-korijandar2-300x300.jpg'

    },
    {
        'name' : 'Vlasac',
        'photo' : '03-luk-vlasac-300x300.jpg'
    },
    {
        'name' : 'Mažuran',
        'photo' : '04-mazuran1-300x300.jpg'
    },
    {
        'name' : 'Menta',
        'photo' : '05-menta-metvica-300x300.jpg'
    },
    {
        'name' : 'Origano',
        'photo' : '06-origano1-300x300.jpg'
    },
    {
        'name' : 'timijan',
        'photo' : '07-timijan-300x300.jpg'
    }
]



# user = User()

# db.session.add(user)


# for j in jars_list:
#     jar = Jar(**j)
#     db.session.add(jar)

# for p in plants_list:
#     plant = Plant(**p)
#     db.session.add(plant)

# db.session.commit()
