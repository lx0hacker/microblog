#!/usr/bin/env python
#-*- coding:utf-8-*-

from app import app
from flask import render_template,flash,redirect,url_for,request
from app.forms import LoginForm
from flask_login import current_user,login_user,login_required,logout_user
from urllib.parse import urlparse
from app.models import User,Post

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts =[ {
        "author": {"username":"johnw"},
        "body":"Hello world"
    }]
    title = 'Home Page'
    return render_template('index.html',title=title,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password_hash(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user,remember=form.remember_me.data) 
        next_page = request.args.get('next')
        if next_page is None or urlparse(next_page).netloc!='':
             next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

