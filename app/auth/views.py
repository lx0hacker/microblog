#!/usr/bin/env python
#coding:utf-8
'''
    @Author:John Wen
    @description:
        
'''

from . import auth
from flask import render_template,redirect,url_for,flash,request
from flask_login import current_user,login_user,logout_user,login_required
from .forms import LoginForm,RegisterForm
from ..models import User
from .. import db

@auth.route('/',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u is not None or u.check_password(form.password.data):
            login_user(u,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or passowrd')
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logout out.')
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegisterForm()
    if form.validate_on_submit():
        u = User(email=form.email.data,username=form.username.data,phone=form.phone.data,password=form.password.data,introduce=form.introduce.data)
        db.session.add(u)
        db.session.commit()
        flash('You can now login')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html',form=form)
