from app import app
from flask import render_template


@app.route('/index2')
def index():
    return render_template('index2.html')


@app.route('/index')
def index2():
    return render_template('index.html')
