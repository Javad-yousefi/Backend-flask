import os

from flask import Flask , render_template , url_for , view
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 

lm = LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir , 'notepad.db')
app.config['SECRET_KEY']='this-is-my-secret'
db = SQLAlchemy(app)
lm.init_app(app)
lm.session_protection = 'strong'
lm.login_view = 'login'

from  .views import *