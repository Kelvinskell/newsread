from flask import Flask
from flask import render_template
import pymysql
pymysql.install_as_MySQLdb()
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = '08dae760c2488d8a0dca1bfb'
app.config['MYSQL_DATABASE_USER'] = 'b983b41c79227f'
app.config['MYSQL_DATABASE_PASSWORD'] = '0a7f7397'
app.config['MYSQL_DATABASE_DB'] = 'heroku_f0275f370907b6e'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-06.cleardb.net'
mysql = MySQL(app)


from application import routes
