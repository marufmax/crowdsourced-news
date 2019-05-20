from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm


@app.route('/')
def index():
    user = {'username': 'Maruf'}
    return render_template('home.html', user=user)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/login', methods=['POST'])
def store():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user: {} '.format(
            form.username.data
        ))
        return redirect('/login')
    return render_template('login.html', title='Sign In')
