from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = { "username": "Ricardo" }
    posts = [
        {
            'autor': {"username": "Juan" },
            'body': "Hermoso día en Asunción"
        },
        {
            'autor': {"username":"Valeria"},
            'body': "Lluvia torrencial en Encarnación"
        }
    ]
    return render_template("index.html", titulo="Home", user=user, posts=posts)
