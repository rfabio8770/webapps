import datetime
from flask import Flask, render_template

# crear una nueva aplicacion web
app = Flask(__name__) 

@app.route("/")
def index():
    nombres = ['Alicia', 'Martín', 'María', 'Juan', 'Sonia']
    return render_template("index.html", names=nombres)