from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo, Regexp


class RegisterForm(Form):
    email = StringField("Email", validators=[Required(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[Required()])
    submit = SubmitField("Create Account")


class LoginForm(Form):
    email = StringField("Email", validators=[Required(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[Required()])
    submit = SubmitField("Sign In")
