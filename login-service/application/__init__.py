from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
from application import database

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'newsread'
mysql = MySQL(app)

from application import routes

