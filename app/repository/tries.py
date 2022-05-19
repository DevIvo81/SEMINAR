# POKUŠAJI

# temperatura = [x/10 for x in range(100, 355, 5)]

# vlaga = [x for x in range(33, 101)]

# db.create_all()

jars_list = [
    {
        'name' : 'Kuhinja',
        'plant_name' : 'Nema Biljke',
        'photo' : 'default.jpg',
        'temperature' : 10,
        'phf' : 7,
        'humidity' : 44
    },
    {
        'name' : 'Terasa',
        'plant_name' : 'Nema Biljke',
        'photo' : 'default.jpg',
        'temperature' : 10,
        'phf' : 7,
        'humidity' : 44
    }
]




plants_list = [
    {
        'name' : 'Bosiljak',
        'photo' : '01-bosiljak1-300x300.jpg',
        'temperature' : 15,
        'phf' : 8,
        'humidity' : 60

    },
    {
        'name' : 'Korijander',
        'photo' : '02-korijandar2-300x300.jpg',
        'temperature' : 20,
        'phf' : 6,
        'humidity' : 40
    },
    {
        'name' : 'Vlasac',
        'photo' : '03-luk-vlasac-300x300.jpg',
        'temperature' : 15,
        'phf' : 8,
        'humidity' : 60
    },
    {
        'name' : 'Mažuran',
        'photo' : '04-mazuran1-300x300.jpg',
        'temperature' : 22,
        'phf' : 5,
        'humidity' : 50
    },
    {
        'name' : 'Menta',
        'photo' : '05-menta-metvica-300x300.jpg',
        'temperature' : 10,
        'phf' : 8,
        'humidity' : 55
    },
    {
        'name' : 'Origano',
        'photo' : '06-origano1-300x300.jpg',
        'temperature' : 23,
        'phf' : 6,
        'humidity' : 38
    },
    {
        'name' : 'Timijan',
        'photo' : '07-timijan-300x300.jpg',
        'temperature' : 20,
        'phf' : 7,
        'humidity' : 39
    }
]

def fill_base():

    for p in plants_list:
        plant = Plant(**p)
        db.session.add(plant)


    for j in jars_list:
        jar = Jar(**j)
        db.session.add(jar)



# db.session.commit()