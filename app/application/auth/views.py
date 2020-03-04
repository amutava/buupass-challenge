import logging

from random import randint

from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, current_user, login_required

from . import auth
from .forms import LoginForm, RegisterForm, ResetPasswordRequestForm, ResetPasswordForm
from .model import User
from .. import db
from ..email import send_email, send_password_reset_email

log = logging.getLogger(__name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user)
            return redirect(url_for("auth.account"))
        flash("Invalid email or password")
        log.info("Invalid email or password")
    return render_template("login.html", login_form=login_form)


@auth.route("/")
@auth.route("/register", methods=["GET", "POST"])
def register():
    user_form = RegisterForm()
    email = user_form.email.data
    password = user_form.password.data
    if user_form.validate_on_submit():
        user = User.query.filter_by(email=user_form.email.data).first()
        if not user:
            user_data = User(email=email, password=password)
            db.session.add(user_data)
            db.session.commit()
            return redirect(url_for("auth.login"))

        flash("email already in use")
        log.info("email already in use")

    return render_template("register.html", user_form=user_form)


@auth.route("/sign_out")
def sign_out():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/password_reset", methods=["GET", "POST"])
def password_reset():
    # if current_user.is_authenticated:
    #     return redirect(url_for("auth.login"))

    pass_reset_form = ResetPasswordRequestForm()
    if pass_reset_form.validate_on_submit():
        user = User.query.filter_by(email=pass_reset_form.email.data).first()
        if user:
            send_password_reset_email(user)

        flash("Check your email for the instructions to reset your password")
        return redirect(url_for("auth.login"))

    return render_template("pwd-reset.html", pass_reset_form=pass_reset_form)


@auth.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("auth.login"))

    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("auth.login"))

    reset_form = ResetPasswordForm()
    if reset_form.validate_on_submit():
        user.set_password(reset_form.password.data)
        db.session.commit()
        flash("Your password has been reset.")
        return redirect(url_for("auth.login"))
    return render_template("pwd-reset.html", reset_form=reset_form)


@auth.route("/account")
# @login_required
def account():
    return render_template("account.html")


@auth.route("/account_bookmarks")
# @login_required
def account_bookmarks():
    return render_template("account-bookmarks.html")


@auth.route("/account_cards")
# @login_required
def account_cards():
    return render_template("account-cards.html")


@auth.route("/account_notifications")
# @login_required
def account_notifications():
    return render_template("account-notifications.html")


@auth.route("/account_travelers")
# @login_required
def account_travelers():
    return render_template("account-travelers.html")


@auth.route("/account_history")
# @login_required
def account_history():
    return render_template("account-history.html")
