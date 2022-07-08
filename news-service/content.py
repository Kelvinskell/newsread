from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/news")
def home_page():
    return render_template('news.html')

@app.route("/")
@app.route("/customize")
def customization_page():
    return render_template('customize.html')
