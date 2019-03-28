from flask import render_template, url_for, redirect
from app import app
import json


@app.errorhandler(404)
def e404(e):
    return render_template('404.html', title='404')

@app.route('/')
def index():
    with open('app/static/articles.json', 'r') as f:
        all_articles = json.load(f)

    zipped_articles = zip(all_articles[::2], all_articles[1::2])

    return render_template('index.html', title="Home", articles=zipped_articles)


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
