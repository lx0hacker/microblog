# Database
## 安装插件
```
pip install flask-sqlalchemy
pip install flask-migrate
```

## 配置Database
config.py
```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:qwe123@192.168.232.132'
SQLALCHEMY_TRACK_MODIFICATIONS=False

```
init.py
```
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy(app)
migrate = Migrate(app,db)

```

## 创建models
```
from app import app,db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64),unique=True,index=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)
```
## 数据库的关系
一对一
一对多
多对多
http://blog.csdn.net/qq_34146899/article/details/52559747 
http://blog.csdn.net/bestallen/article/details/52601457 

## migrate 过程
```
1. flask db init
2. flask db migrate -m "xxx"
3. flask db upgrade

如果要回滚数据
4. flask db downgrade
```