#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(128),unique=True,index=True)
    password_hash = db.Column(db.String(129))
    