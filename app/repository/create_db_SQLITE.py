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



# db.session.add(user)


# for j in jars_list:
#     jar = Jar(**j)
#     db.session.add(jar)

# for p in plants_list:
#     plant = Plant(**p)
#     db.session.add(plant)

# db.session.commit()