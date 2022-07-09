from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
from application import database
database.create_database()
database.create_table()

app = Flask(__name__)
app.config['SECRET_KEY'] = '08dae760c2488d8a0dca1bfb'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'newsread'
mysql = MySQL(app)

from application import routes

