from datetime import datetime
from hashlib import md5
from flask_login import UserMixin
from werkzeug.security import check_password_hash , generate_password_hash

from Notepad import db 

class User(db.Model , UserMixin):
    id = db.Column( db.Integer , primary_key=True)
    username = db.Column( db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwordHash = db.Column(db.String(120))
    notes = db.relationship('Note',backref = 'user' , lazy = 'dynamic')

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def setPassword(self , password)
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self , password)
        return check_password_hash(self.passwordHash , password)

    @staticmethod
    def getByEmail(email):
        return User.query.filter_by(email=email).first()

    def __init__(self , username , email , password):
        self.username = username
        self.email = email
        self.setPassword(password)

class Note (db.Model):
    id = db.Column( db.Integer , primary_key=True )
    title = db.Column( db.String(120), unique=True, nullable=False )
    content = db.Column( db.Text , unique=True, nullable=False )
    lastModified = db.Column( db.DateTime)
    userId = db.Column(db.Integer , db.ForeignKey('user.id'))

    

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self , title , content , lastModified , userId):
        self.title = title
        self.content = content
        self.lastModified = datetime.utcnow()
        self.userId=userId