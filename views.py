from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenId="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
