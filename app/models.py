#!/usr/bin/env python
#-*- coding:utf-8 -*-
from app import app,db
from datetime import datetime
'''
u.posts.all()
backref执行了一句sql语句

执行u.posts的时候执行：
SELECT post.id AS post_id, post.title AS post_title, post.body AS post_body, pos
t.timestamp AS post_timestamp, post.user_id AS post_user_id
FROM post
WHERE %(param_1)s = post.user_id

select ===> 直接返回结果列表
dynamic ===> 返回一个query对象
'''

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64),unique=True,index=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post',backref='author',lazy='dynamic')

    def __repr__(self):
        return "<User {}>".format(self.username)

class Post(db.Model):
    __tablename__='post'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(120),unique=True,index=True)
    # 140 是多少个字符？
    body = db.Column(db.String(140))
    # 这里default放的是一个函数，也就是没有值的话，会自动去执行这个函数，得到一个值。
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    # 这里的user.id user是表名，id是表的字段。
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Post {}>".format(self.title)
