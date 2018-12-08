from flask import render_template, url_for, redirect
from app import app


@app.errorhandler(404)
def e404(e):
    return render_template('404.html', title='404')

@app.route('/')
def index():
    return render_template('index.html', title="Home")


@app.route('/articles/<name>/')
def articles(name):
    try:
        r = render_template('articles/{}.html'.format(name), title=name.replace('_', ' ').title())
    except:
        r = render_template('404.html', title='404')

    return r


@app.route('/articles/')
def articles_re():
    return redirect(url_for('index'))
