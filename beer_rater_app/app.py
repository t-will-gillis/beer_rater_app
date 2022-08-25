from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super33secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


# login_manager = LoginManager()
# login_manager.init_app(app)




import routes, models