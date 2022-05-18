from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .repository import get_all_readings

#region CONFIGS
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/pics'
# SQLITE DB CONNECTION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/DEJTA.sqlite'

# MySQL DB CONNECTION
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/our_users'


app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mojsupertajnikljuc'

moment = Moment(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from . import routes
