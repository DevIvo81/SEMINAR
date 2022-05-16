from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#region CONFIGS
app = Flask(__name__)

# SQLITE DB CONNECTION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/DEJTA.sqlite'

# MySQL DB CONNECTION
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/our_users'



app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mojsupertajnikljuc'

moment = Moment(app)

db = SQLAlchemy(app)

from . import routes