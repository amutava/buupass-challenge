from random import randint

from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user

from . import auth
from .forms import LoginForm, RegisterForm
from .model import users


@auth.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = {}
        for user in users:
            if user["email"] == login_form.email.data:
                user = user
        if user and user["password"] == login_form.password.data:
            return redirect(url_for("buupass.index"))

        flash("Invalid email or password")
    return render_template("login.html", login_form=login_form)


@auth.route("/")
@auth.route("/register", methods=["GET", "POST"])
def register():
    user_form = RegisterForm()
    email = user_form.email.data
    password = user_form.password.data
    if user_form.validate_on_submit():
        build_user_data = {
            "id": randint(4, 10000),
            "email": email,
            "password": password,
        }
        users.append(build_user_data)
        return redirect(url_for("auth.login"))

    return render_template("register.html", user_form=user_form)


@auth.route("/sign_out")
def sign_out():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/password_reset")
def password_reset():
    return render_template("pwd-reset.html")


@auth.route("/account")
def account():
    return render_template("account.html")


@auth.route("/account_bookmarks")
def account_bookmarks():
    return render_template("account-bookmarks.html")


@auth.route("/account_cards")
def account_cards():
    return render_template("account-cards.html")


@auth.route("/account_notifications")
def account_notifications():
    return render_template("account-notifications.html")


@auth.route("/account_travelers")
def account_travelers():
    return render_template("account-travelers.html")


@auth.route("/account_history")
def account_history():
    return render_template("account-history.html")
