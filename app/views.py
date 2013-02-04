from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm

from app import app, db, lm, oid
from models import User, ROLE_USER, ROLE_ADMIN


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])

    return render_template('login.html',
                title = 'Sign In',
                form = form,
                providers = app.config['OPENID_PROVIDERS'])


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Dimas' }
    posts = [ #fake array of posts
        {
            'author': { 'nickname': 'John'},
            'body': "It's raining today"
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
        ]
    return render_template('index.html',
                title = 'Home',
                user = user,
                posts = posts)


@lm.user_loader
def load_user(id):              # function will be used by Flask-Login
    return User.query.get(int(id))
