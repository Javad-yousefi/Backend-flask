import os
from flask import Flask , request , escape , render_template , url_for
from flask_sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
print('sqlite:///'+ os.path.join(basedir , 'db\noter.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir , 'noter.db')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column( db.Integer , primary_key=True)
    username = db.Column( db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    

class Note(db.Model):
    id = db.Column( db.Integer , primary_key=True )
    title = db.Column( db.String(120), unique=True, nullable=False )
    content = db.Column( db.Text , unique=True, nullable=False )
    lastModified = db.Column( db.Date)
    



title="HOME" 

@app.route('/')
def hello():
   return render_template( "index.html " , titleHeader = title, title=title)

if __name__ == "__main__":
    app.run(debug=True)