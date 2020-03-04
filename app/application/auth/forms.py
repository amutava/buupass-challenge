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


class ResetPasswordRequestForm(Form):
    email = StringField("Email", validators=[Required(), Length(1, 64), Email()])
    submit = SubmitField("Reset Password")


class ResetPasswordForm(Form):
    password = PasswordField("Password", validators=[Required()])
    password2 = PasswordField(
        "Repeat Password", validators=[Required(), EqualTo("password")]
    )
    submit = SubmitField("Request Password Reset")
