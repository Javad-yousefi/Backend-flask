from flask import Flask
from flask import render_template

app=Flask(__name__)
model = "javad YU"

@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/home')
def index():
    return render_template('home.html',name=model)

@app.route('/name/<name>')
def sayHello(name):
    return render_template('name.html',name=name)


if __name__ == "__main__":
    app.run(debug=True)