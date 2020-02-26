from flask import Blueprint

buupass = Blueprint('buupass', __name__)

from . import views
