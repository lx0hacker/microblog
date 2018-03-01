#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,AnonymousUserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(128),unique=True,index=True)
    phone = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(256))
    introduce = db.Column(db.Text(256))
    last_seen = db.Column(db.DateTime(),default=datetime.utcnow)
    # 一个对象只有一个role，所以一个对象里面只要保持id就好了
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)


    def __init__(self, **kw):
        super(User, self).__init__(**kw)
        if self.role is None:
            if self.email == '403481704@qq.com':
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()


    def can(self,permissions):
        return self.role is not None and \
               (self.role.permissions & permissions) == permissions
    def is_administrator(self):
        return self.can(Permission.ADMINISTER)
    def __repr__(self):
        return '<User: {}>'.format(self.username)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute!')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)


class AnonymousUser(AnonymousUserMixin):
    def can(self,permissions):
        return False
    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser

class Role(db.Model):
    __tablename__= 'role'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),index=True,unique=True)
    # 一个对象，一个role里面有多个user，所以这里保存了所有的user。所以，如果这里设置了userlist为false的话，就是一对一了。
    users = db.relationship('User',backref='role')
    default = db.Column(db.Boolean,default=False,index=True)
    permissions = db.Column(db.Integer)

    @staticmethod
    def insert_roles():
        roles = {
            'User':(Permission.FOLLOW |
                    Permission.COMMENT |
                    Permission.WRITE_ARTICLE,True),
            'Moderator':(Permission.FOLLOW |
                         Permission.COMMENT |
                         Permission.WRITE_ARTICLE |
                         Permission.MODERATE_COMMENTS,False),
            'Administator':(0xff,False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()


    def __repr__(self):
        return "<Role: {}>".format(self.name)

class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLE = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80



