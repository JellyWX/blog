from flask import render_template, url_for, redirect
from app import app


@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/articles/<name>/')
def articles(name):
    return render_template('articles/{}.html'.format(name))

@app.route('/articles/')
def articles_re():
    return redirect(url_for('index'))
