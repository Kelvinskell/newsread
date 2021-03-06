from flask import Flask
from flask import render_template
import pymysql
pymysql.install_as_MySQLdb()
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '08dae760c2488d8a0dca1bfb'
app.config['MYSQL_DB'] = 'heroku_f0275f370907b6e'
app.config['MYSQL_USER'] = 'b983b41c79227f'
app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
app.config['MYSQL_PASSWORD'] = os.getenv('DATABASE_PASSWORD')
mysql = MySQL(app)


from application import routes
