from flask import render_template, url_for
from app import app


@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/articles/<name>')
def articles(name):
    return render_template('{}.html'.format(name))
