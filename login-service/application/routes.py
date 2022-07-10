from application import app
from flask import render_template, redirect, url_for
from application import mysql
import MySQLdb.cursors
from application.forms import RegisterForm

# DEFINE SQL STATEMENTS
CREATE_USER = """
INSERT INTO user
(username, email_address, password)
VALUES (%s, %s, %s)
"""


@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email_address = form.email_address.data
        password1 = form.password1.data
        cursor = mysql.connection.cursor()
        cursor.execute(CREATE_USER, (username, email_address, password1))

        # save to database
        mysql.connection.commit()

        # close cursor
        cursor.close()
        return '<h1>You have successfully registered</h1>'

    return render_template('register.html', form=form)
