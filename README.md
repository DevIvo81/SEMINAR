# IZ_PyFlora
## Pametne teglice za cvijeće
## Autor: Ivo Zelić
## Platforma izrade: Python - Flask

### Upute za pokretanje aplikacije:

- prvo instalirati virtualno okruženje unosom naredbe:
    "py -m venv venv_pyflora"

- direktorij venv_pyflora/ je naveden u ".gitignore" datoteci

- potom instalirati module unosom naredbe:
    "pip install -r requirements.txt"

- u Visual Studio Code postaviti interpreter s oznakom('venv_pyflora':venv)       \venv_pyflora\Scripts\Python.exe

- pokrenuti aplikaciju upisom naredbe: 
    "py run.py"



### O IZ_PyFlora aplikaciji: 

- pokretanje aplikacije vas vodi na Login stranicu. U aplikaciju se ne može ući bez autentifikacije korisnika. U bazi postoji jedan korisnik.
name : Korisnik
password : lozinka

- ako se želite registrirati na dnu je link na stranicu za registraciju.

- na glavnom ekranu je prikaz posuda i senzora posude ('offline' ako u posudi nema biljke)

- CHANGE SENSOR VALUES vrši nasumičnu promjenu vrijednosti senzora temperature, pH i vlage u svim posudama.

- u rubriku 'Add New Jar' se upisuje lokacija posude koja se dodaje

- klik na 'Delete' vodi na stranicu posude za brisanje kao dodatni korak prije potvrde.

- klik na 'Details' vodi na stranicu posude koja je odabrana. U posudu je moguće staviti biljku iz baze biljaka i isprazniti posudu, dok 'SYNC JAR' nasumično mijenja simulirane vrijednosti senzora posude te uspoređuje mjerenja temperature, pH i vlage senzora s posude/a te prema dostatnosti odnosno manjku u usporedbi s podacima o biljci određuje status. Usporedbe su prikazane i u histogramu sa strane. Ako nema biljke u posudi histogram je prazan.

- klik na ime biljke otvara novi prozor s podacima o biljci.

- u bazi je 11 začinskih biljaka

- moguće je dodavati nove biljke i pripadajuću im sliku

- biljke je moguće i brisati iz baze, ali molim da ako se taj link koristi da se podaci o biljci kopiraju i da se biljka ponovno doda u bazu.

- karakteristike biljaka su odokativno napisane


## Izvori 

- podaci o biljkama - https://www.agroklub.com/

- 404 template - https://codepen.io/1832Manaswini/pen/Vwezyjx

- Smart Pot image (vidljiv vodeni žig na default.jpg)- https://www.dreamstime.com/smart-pot-watering-icon-simple-color-outline-vector-elements-automated-farming-icons-ui-ux-website-mobile-image189609777#_

- ostali predlošci - https://getbootstrap.com/





