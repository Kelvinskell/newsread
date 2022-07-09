from application import app
from flask import render_template
from application import mysql
import MySQLdb.cursors
from application.forms import RegisterForm

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)
