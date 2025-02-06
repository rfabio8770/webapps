from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Ingreso solicitado para el usuario {}, recordar={}".format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for("index"))
    return render_template("login.html", titulo="Iniciar Sesión", form=form)