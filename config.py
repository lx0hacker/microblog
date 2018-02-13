import os

class Configqa(object):
    SECRET_KEY = 'qwe123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:qwe123@192.168.232.132/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Configcm(object):
    SECRET_KEY = 'qwe123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:qwe123@127.0.0.1/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

