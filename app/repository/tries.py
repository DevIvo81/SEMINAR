# POKUŠAJI




# temperatura = [x/10 for x in range(100, 355, 5)]

# vlaga = [x for x in range(33, 101)]

# db.create_all()

user_list = [
    {
    'name': 'Korisnik',
    'password': 'Lozinka'
    }
]

jars_list = [
    {
        'name' : 'Kuhinja',
        'plant_name' : 'Plantless',
        'photo' : 'default.jpg',
        'temperature' : 10,
        'phf' : 7,
        'humidity' : 44
    },
    {
        'name' : 'Terasa',
        'plant_name' : 'Plantless',
        'photo' : 'default.jpg',
        'temperature' : 10,
        'phf' : 7,
        'humidity' : 44
    }
]


plants_list = [
    {
        'name' : 'Bosiljak',
        'photo' : '01-bosiljak-300x300.jpg',
        'details' : 'Bosiljak je biljka od davnina poznata kao začin. Smatra se da potječe iz Indije, a danas se najviše upotrebljava u Francuskoj i Italiji. To je jednogodišnja zeljasta biljka koja pripada porodici usnača (Lamiaceae, Labiateae). U obliku čaja bosiljak se koristi kao sredstvo za umirenje i kod probavnih problema, a ima i izraženo antiseptično svojstvo. Često se upotrebljava prilikom inhalacije dišnih puteva. Stabljika bosiljka sadrži 0,5 – 1,5 % eteričnog ulja, u kojemu ima najviše metilkavikola (55%), estragola i eugenola. Karakterističan miris i aromu biljci daje upravo kemijska tvar eugenol.',
        'temperature' : 15,
        'phf' : 8,
        'humidity' : 60

    },
    {
        'name' : 'Korijandar',
        'photo' : '02-korijandar-300x300.jpg',
        'details' : 'Korijandar je jednogodišnja zeljasta biljka. Smatra se da je korijandar uveden u proizvodnju u 16. stoljeću, ali to je biljka koja se spominje već u Bibliji. Koristi se plod biljke, koji sadrži etarsko ili eterično ulje. Rjeđe su u uporabi listovi, stabljika i korijen, pri čemu listovi mogu ispuštati neugodan miris. Korijandar se upotrebljava u industriji likera, peciva i suhomesnatih proizvoda, a najveću pak primjenu pronalazi u proizvodnji eteričnog ulja za kozmetičku industriju.',
        'temperature' : 20,
        'phf' : 6,
        'humidity' : 40
    },
    {
        'name' : 'Vlasac',
        'photo' : '03-luk-vlasac-300x300.jpg',
        'details' : 'Luk vlasac ima listove koji su cjevasti, šuplji, dugi 20 - 25 cm koji formiraju više ili manje kompaktni busen na zajedničkom rizomu, koji može imati do 80 izboja. U prvoj godini takva biljka ne cvate, a u drugoj godini nakon mirovanja i vernalizacije (poticajno djelovanje hladnoće na stvaranje cvjetova) iz svih starijih izboja izbije cvjetna biljka visoka oko 30 cm, koja na vrhu nosi cvat (štitac s ružičastim ili ljubičastim cvjetovima). Sjeme brzo gubi klijavost, pa se koristi samo jednogodišnje sjeme.',
        'temperature' : 8,
        'phf' : 8,
        'humidity' : 60
    },
    {
        'name' : 'Mažuran',
        'photo' : '04-mazuran-300x300.jpg',
        'details' : 'Mažuran se u umjerenoj klimi uzgaja kao jednogodišnja biljka, koja u toplijim, mediteranskim područjima može živjeti kao višegodišnja. Pripada porodici usnača (Lamiaceae /Labiaceae). U starom se Egiptu uzgajao kao sveta biljka, a Grci i Rimljani smatrali su ga simbolom sreće. U Europi se uzgaja od 14. stoljeća. Mažuran se najčešće upotrebljava kao začin i to nadzemni dio biljke. Ulje je svijetlo-žute boje i ugodnog mirisa.',
        'temperature' : 22,
        'phf' : 5,
        'humidity' : 50
    },
    {
        'name' : 'Menta',
        'photo' : '05-menta-metvica-300x300.jpg',
        'details' : 'Mentu ili Metvicu karakterizira ugodan miris mentola, a jedna je od najvažnijih ljekovitih biljaka za proizvodnju eteričnog ulja, lijekova i čajeva. Djeluje osvježavajuće i umirujuće i ublažava smetnje pri disanju. Kao Lijek se upotrebljava list i stabljika s listovima i cvatovima. Mentol je osnovni sastojak eteričnog ulja, ima jako baktericidno djelovanje. Upotrebljava u farmaceutskoj, kozmetičkoj i prehrambenoj industriji. Površine se sve više šire zbog velike potražnje za suhim listom i eteričnim uljem. Danas se proizvode crna, bijela i zelena metvica. Na području Hrvatske raširen je oblik metvice rubescen. Višegodišnja je biljka koja prezimljuje pomoću vriježa.',
        'temperature' : 10,
        'phf' : 8,
        'humidity' : 55
    },
    {
        'name' : 'Origano',
        'photo' : '06-origano-300x300.jpg',
        'details' : 'Origano je višegodišnja, zeljasta biljka iz porodice usnača (Lamiaceae /Labiaceae). Budući da se radi o kulturi toplog podneblja, na našem je području najzastupljenija u području Mediterana. Osobito je zatupljena u Grčkoj, Italiji, Izraelu i drugim mediteranskim zemljama. Prvenstveno se origano koristi kao cijenjeni začin u kulinarstvu i mesnoj industriji, ali poznati su njegovi blagotvorni učinci za tegobe probavnog sustava.',
        'temperature' : 23,
        'phf' : 6,
        'humidity' : 38
    },
    {
        'name' : 'Timijan',
        'photo' : '07-timijan-300x300.jpg',
        'details' : 'Timijan je višegodišnja, 20-ak cm visoka biljka jakog i ugodnog mirisa koja sadrži mnogo eteričnog ulja. Ne podnosi kisela tla. Voli mnogo sunca. Razmnožava se sjetvom ili dijeljenjem busena.',
        'temperature' : 20,
        'phf' : 7,
        'humidity' : 39
    },
    {
        'name' : 'Kadulja',
        'photo' : '08-kadulja-300x300.jpg',
        'details' : 'Kadulja ima raznoliku namjenu, no najčešće se upotrebljava za dobivanje eteričnog ulja. Čaj od kadulje služi za obloge za rane te za ispiranje usta i grla radi dezinfekcije. Upotrebljava se u kozmetičkoj, farmaceutskoj i prehrambenoj industriji. Ima jaki fiziološki utjecaj na vitalne organe čovjeka. Potražnja za eteričnim uljem kadulje u svijetu i kod nas je sve veća, pa se obnavljaju stari nasadi i stvaraju novi.',
        'temperature' : 20,
        'phf' : 6,
        'humidity' : 33
    },
    {
        'name' : 'Lavanda',
        'photo' : '09-lavanda-300x300.jpg',
        'details' : 'Lavanda je vrlo omiljena ukrasna biljka, a sve se više uzgaja i plantažno. Nema velikih zahtijeva u pogledu kvalitete tla, uzgoj joj je vrlo ekonomičan, a može poslužiti i kao dobra ispaša za pčele. U našoj zemlji najviše lavande se proizvodi na Hvaru. Ime lavanda potječe od latinske riječi lavare, što znači kupati se, a objašnjava osnovnu namjenu suhog cvijeta i lavandina, eteričnog ulja. Eterično ulje prave lavande upotrebljava se za proizvodnju parfema i kolonjske vode. Za proizvodnju sapuna upotrebljava se jeftinije eterično ulje hibridne lavande. Ljekovito svojstvo lavande sastoji se u smanjenju živčane napetosti pri migreni i neuralgiji. Ublažava grčeve i pomaže u zacjeljivanju rana.',
        'temperature' : 22,
        'phf' : 5,
        'humidity' : 30
    },
    {
        'name' : 'Stevija',
        'photo' : '10-stevija-300x300.jpg',
        'details' : 'Stevija je višegodišnja zeljasta biljka iz porodice glavočika (Asteraceae). Najbolje uspijeva u područjima mediteranske (suptropske) i umjereno kontinentalne klime, a u hladnijim se područjima uzgaja kao jednogodišnja biljka. U listovima stevija sadržava tvari steviozid i rebaudiozid A te još šest drugih glikozida koji su uzrokom izuzetno slatkog okusa. Listovi su vrlo slatki, trideset puta slađi od šećera saharoze. U uvjetima veće količine sunčeve svjetlosti i viših temperatura, biljka će proizvoditi veću količinu lisne mase, radi koje se i uzgaja.',
        'temperature' : 18,
        'phf' : 8,
        'humidity' : 66
    },
]

def fill_base():

    for u in user_list:
        user = User(**u)
        db.session.add(user)
    
    for p in plants_list:
        plant = Plant(**p)
        db.session.add(plant)

    for j in jars_list:
        jar = Jar(**j)
        db.session.add(jar)



# db.session.commit()