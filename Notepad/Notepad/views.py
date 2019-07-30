from flask import url_for , render_template
from flask_login import current_user

from . import app , lm 
from .models import User , Note

@lm.user_loader
def load_user(userId):
    return User.get(userId)

@app.route('/')
def index():
   return render_template('index.html')