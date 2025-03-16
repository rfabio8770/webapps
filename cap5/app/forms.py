from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from wtforms.validators import Email
from wtforms.validators import EqualTo
import sqlalchemy as sa
from app import db
from app.models import User
class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contrasenha", validators=[DataRequired()])
    remember_me = BooleanField("Recuerdame")
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Contrasenha", validators=[DataRequired()])
    password2 = PasswordField("Repetir Contrasenha", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Registrarse")

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError("Por favor use un nombre de usuario diferente")

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError("Por favor use un email diferente")