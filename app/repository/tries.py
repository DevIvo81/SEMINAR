# POKUŠAJI

temperatura = [x/10 for x in range(100, 355, 5)]

vlaga = [x for x in range(33, 101)]

# db.create_all()

jars_list = [
    {
        'name' : 'Prazna posuda 1',
        'plant_name' : 'Nema Biljke',
        'photo' : 'default.jpg',
        'temperature' : 10,
        'pH_F' : 7,
        'humidity' : 44
    },
    {
        'name' : 'Prazna posuda 2',
        'plant_name' : 'Nema Biljke',
        'photo' : 'default.jpg',
        'temperature' : 10,
        'pH_F' : 7,
        'humidity' : 44
    }
]

# for j in jars_list:
#     jar = Jar(**j)
#     db.session.add(jar)
# db.session.commit()



plants_list = [
    {
        'name' : 'Bosiljak',
        'photo' : '01-bosiljak1-300x300.jpg',
        'temperature' : 15,
        'pH_F' : 8,
        'humidity' : 60

    },
    {
        'name' : 'Korijander',
        'photo' : '02-korijandar2-300x300.jpg',
        'temperature' : 20,
        'pH_F' : 6,
        'humidity' : 40
    },
    {
        'name' : 'Vlasac',
        'photo' : '03-luk-vlasac-300x300.jpg',
        'temperature' : 15,
        'pH_F' : 8,
        'humidity' : 60
    },
    {
        'name' : 'Mažuran',
        'photo' : '04-mazuran1-300x300.jpg',
        'temperature' : 22,
        'pH_F' : 5,
        'humidity' : 50
    },
    {
        'name' : 'Menta',
        'photo' : '05-menta-metvica-300x300.jpg',
        'temperature' : 10,
        'pH_F' : 8,
        'humidity' : 55
    },
    {
        'name' : 'Origano',
        'photo' : '06-origano1-300x300.jpg',
        'temperature' : 23,
        'pH_F' : 6,
        'humidity' : 38
    },
    {
        'name' : 'timijan',
        'photo' : '07-timijan-300x300.jpg',
        'temperature' : 20,
        'pH_F' : 7,
        'humidity' : 39
    }
]

# for p in plants_list:
#     plant = Plant(**p)
#     db.session.add(plant)
# db.session.commit()

# for p in plants_list:
#     plant = Plant(
#         name=p['name'],
#         photo=p['photo']
#     )
#     db.session.add(plant)
#     db.session.commit()