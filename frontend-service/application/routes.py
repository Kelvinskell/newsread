from flask import render_template
from application import app


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
