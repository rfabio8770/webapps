from urllib.parse import urlsplit
import sqlalchemy as sa
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from app.models import User
from app import db
from flask import render_template, flash, redirect, url_for
from flask import request
from app import app
from app.forms import LoginForm, RegistrationForm

@app.route("/")
@app.route("/index")
@login_required
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
    return render_template("index.html", titulo="Home", posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash("Usuario o contraseña inválidos")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)   
    return render_template("login.html", titulo="Iniciar Sesión", form=form)
    '''form = LoginForm()
    if form.validate_on_submit():
        flash("Ingreso solicitado para el usuario {}, recordar={}".format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for("index"))
    return render_template("login.html", titulo="Iniciar Sesión", form=form) '''
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Felicitaciones, ahora estas registrado")
        return redirect(url_for("login"))
    return render_template("register.html", titulo="Registrarse", form=form)