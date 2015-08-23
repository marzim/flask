from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    posts = [
        {
            'author': {'nickname' : 'marvin'},
            'body' : 'The three black wizard!'
        },
        {
            'author': {'nickname' : 'matt'},
            'body' : 'The quick brown fox jump over the lazy dog!'
        }
    ]
    user = {'nickname':'carlos'}
    return render_template('index.html',title='Home',user=user,posts=posts)
