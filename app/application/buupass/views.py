from . import buupass
from flask import render_template, redirect, url_for, request, flash, session


@buupass.route('/')
@buupass.route('/home')
def index():
    return render_template('index.html')
