from . import buupass
from flask import render_template, redirect, url_for, request, flash, session


@buupass.route("/home")
def index():
    return render_template("index.html")


@buupass.route("/search_homes")
def search_homes():
    pass


@buupass.route("/search_hotels")
def search_hotels():
    pass


@buupass.route("/search_cars")
def search_cars():
    pass


@buupass.route("/search_experiences")
def search_experiences():
    pass


@buupass.route("/search_flights")
def search_flights():
    pass
