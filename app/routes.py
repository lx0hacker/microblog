#!/usr/bin/env python
#-*- coding:utf-8-*-

from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {
        "username":'johnw',
    }
    posts =[ {
        "author": {"username":"johnw"},
        "body":"Hello world"
    }]
    title = 'Home Page'
    return render_template('index.html',title=title,user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html',form=form)