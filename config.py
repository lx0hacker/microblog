import os

class Config:
    SECRET_KEY = 'qwe123'
    SQLALCHCEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:qwe123@192.168.232.132/microblog'

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

config = {
    'development':DevelopConfig,
    'testing':TestingConfig,
    'prod':ProdConfig,
    'default':DevelopConfig,
}