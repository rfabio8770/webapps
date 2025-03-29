from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Usuario, Rol, Actividad
from forms import LoginForm, RegisterForm, ActividadForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route("/")
def index():
    actividades = Actividad.query.all()
    return render_template("index.html", actividades=actividades)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("index"))
        flash("Usuario o contraseña incorrectos")
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        usuario = Usuario(username=form.username.data, password=hashed_password, rol_id=1)
        db.session.add(usuario)
        db.session.commit()
        flash("Registro exitoso, inicia sesión")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/crear_actividad", methods=["GET", "POST"])
@login_required
def crear_actividad():
    form = ActividadForm()
    if form.validate_on_submit():
        actividad = Actividad(
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            fecha=datetime.utcnow(),
            usuario_id=current_user.id
        )
        db.session.add(actividad)
        db.session.commit()
        flash("Actividad creada")
        return redirect(url_for("index"))
    return render_template("actividades.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
