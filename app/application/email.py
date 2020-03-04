import os

from threading import Thread

from flask_mail import Message
from flask import render_template

from . import mail, create_app
from .auth.model import User


app = create_app("default")

sender = os.environ.get("MAIL_USERNAME")


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, body, html, **kwargs):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = body
    msg.html = html
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(
        "[Buupass] Reset Your Password",
        sender=sender,
        recipients=[user.email],
        body=render_template("email/reset_password.txt", user=user, token=token),
        html=render_template("email/reset_password.html", user=user, token=token),
    )
