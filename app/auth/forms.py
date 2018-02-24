#!/usr/bin/env python
#coding:utf-8
'''
    @Author:John Wen
    @description:
        
'''
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,PasswordField,TextAreaField,ValidationError
from wtforms.validators import DataRequired,Length,Email,EqualTo,Regexp
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('email:',validators=[DataRequired(),Email(),Length(1,64)])
    password = PasswordField('password:',validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    email = StringField('email:',validators=[DataRequired(),Email(),Length(1,64)])
    password = PasswordField('password:',validators=[DataRequired(),EqualTo('password2',message='Password must match!')])
    password2 = PasswordField('confirm password',validators=[DataRequired()])
    username = StringField('username',validators=[Length(1,64),Regexp('^[a-zA-Z0-9_.]+$',0,
                                                                      'username must have only letters,'
                                                                      'numbers ,dots,or underscores'),DataRequired()])
    phone = StringField('phone number',validators=[DataRequired()])
    introduce = TextAreaField('Self introduction:',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already register!')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already reigster!')





