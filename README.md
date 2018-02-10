# Hello Wrold
### 安装python
### 安装开发环境
```
midir microblog
python -m venv venv
source venv/bin/activate

pip install flask

mkdir app
touch __init__.py
```
### __init__.py
```
from flask import Flask
app = Flask(__name__)
from app import routes
```
1. 引进 flask 框架
2. 创建一个实例app， __name__ flask使用这个属性来链接其他资源，比如templates文件夹
3. import 语句放在最后，是因为在routes里面也要引入app这个实例，避免循环引入。
4. 创建routes.py 

### routes.py
```
from app import app
@app.route('/')
def index():
    return "Hello world"
```
设置启动脚本： microblog.py

### microblog.py
```
from app import app
```
### 启动
```
export FLAKSK=microblog.py
export FLASK_DEBUG=1
flask run
```
