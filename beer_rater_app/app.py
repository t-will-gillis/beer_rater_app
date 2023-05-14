from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = 'in3Thisworlditsjustus#'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('postgresql://lvfwtdrghprwqn:9af28eb0a7e5fb9f4ed3d3d261a03e1256a1d0088806edcf0323ed758f4d074d@ec2-52-207-90-231.compute-1.amazonaws.com:5432/d910v946viofia') or 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


import routes, models