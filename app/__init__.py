import os
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from .repository import get_all_readings, generate_chart

#region CONFIGS
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False
app.config['UPLOAD_FOLDER'] = '/static/pics/'
# SQLITE DB CONNECTION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/DEJTA.sqlite'

# MySQL DB CONNECTION
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/our_users'


# app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'mojsupertajnikljuc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

moment = Moment(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from . import routes
