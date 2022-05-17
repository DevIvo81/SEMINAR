class User(db.Model):
    __tablename__ = 'biljka'
    id = db.Column(db.Integer, db.ForeignKey)
    name = db.Column(db.String, db.ForeignKey)
    password = db.Column(db.String, db.ForeignKey)


class Biljka(db.Model):
    __tablename__ = 'biljka'
    id = db.Column(db.Integer)
    
    naziv = db.Column(db.String)
    foto = db.Column(db.String) # ... putanja do slike
    
    posude = db.relationship('Posuda', backref=('biljka'))
    

class Posuda(db.Model):
    __tablename__ = 'posuda'
    id = db.Column(db.Integer, db.ForeignKey)
    
    naziv = db.Column(db.String, db.ForeignKey)
    
    # ...ForeignKey mora biti isti tip podatka na koji se veže
    biljka_id = db.Column(db.Integer, db.ForeignKey('biljka.id'))
    
    
'''
Jedna funkcija dohvaća sve posude


onda za svaku posudu bira iz popisa

'''
