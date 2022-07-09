from application import app
from application import mysql
import MySQLdb.cursors
from application.forms import RegisterForm

@app.route('/register')
def register_page():
    form = RegisterForm()
