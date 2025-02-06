from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contrasenha", validators=[DataRequired()])
    remember_me = BooleanField("Recuerdame")
    submit = SubmitField('Sign in')