from application import app
from flask import render_template, redirect, url_for, flash
from application import mysql
import MySQLdb
import MySQLdb.cursors
from application.forms import RegisterForm

# DEFINE SQL STATEMENTS
CREATE_USER = """
INSERT INTO user
(username, email_address, password)
VALUES (%s, %s, SHA1(%s))
"""


@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    
    # Flash Error messages
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error: {err_msg}')

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
    return render_template('register.html', form=form)
