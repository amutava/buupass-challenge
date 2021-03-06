import os

from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from config import config


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
login_manager = LoginManager()
db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()

# can be set to basic ,None or strong
# it keeps track of the browser the user is using
login_manager.session_protection = "None"
# The login_view
# a blueprint, it needs to be prefixed with the blueprint name.
login_manager.login_view = "auth.login"


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config["SECRET_KEY"] = "hard to guess string"
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from .buupass import buupass as buupass_blueprint

    app.register_blueprint(buupass_blueprint)

    return app
