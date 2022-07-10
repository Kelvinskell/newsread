from application import app
from flask import render_template, redirect, url_for, flash
from application import mysql
import MySQLdb
import MySQLdb.cursors
from application.forms import RegisterForm, LoginForm

# DEFINE SQL STATEMENTS
CREATE_USER = """
INSERT INTO user
(username, email_address, password)
VALUES (%s, %s, SHA1(%s))
"""


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    
    # Flash Error messages
    if form.validate_on_submit():
        username = form.username.data
        email_address = form.email_address.data
        password1 = form.password1.data
        cursor = mysql.connection.cursor()

        # MYSQL Operational Errors
        try:
            cursor.execute(CREATE_USER, (username, email_address, password1))
        except MySQLdb.OperationalError:
            return '''
                   <hr />
                   <h1><strong>Connection Time out</strong></h1>
                   <hr />
                   <br>
                   <h2>Return To Previous Page</h2>
                   '''

        # Save to database
        mysql.connection.commit()

        # Close cursor
        cursor.close()
        return '<h1>You have successfully registered</h1>'

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg[0]}')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # Execute SQL Query to validate details
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(f"SELECT * FROM user WHERE username = '{username}' AND password = SHA1('{password}')")
        account = cursor.fetchone()

        if account:
             flash(f'Success! You are logged in as {username}', category='success')
             return '<h1>News Page</h1>'
        else:
            flash('Username or Password incorrect. Please try again.', category='danger')
    return render_template('login.html', form=form)

