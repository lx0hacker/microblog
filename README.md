# templates
### 什么是templetas
> 我们不可能每个函数都去写html，我们需要有一个html，然后我们往这个html里面传入参数，从而构成一个完整的页面。

* 如何做？
> 新建 templates 文件夹， 因为我们已经在 app/__init__.py 里面使用了 __name__ 属性。所以flask 会自己去寻找 在当前文件夹里面 叫做 templates 的文件夹

### templates文件
```
cd app
mkdir templates
touch base.html
touch index.html
```
### routes.py
```
#!/usr/bin/env python
#-*- coding:utf-8-*-

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    # mock
    user = {
        "username":'johnw',
    }
    posts =[{
        "author": {"username":"johnw"},
        "body":"Hello world"
    }]
    title = 'Home Page'
    return render_template('index.html',title=title,user=user,posts=posts)

```
### base.html
> 首先在我们程序中肯定有某部分是不变的，比如导航栏，比如页面底部。这个时候我们需要引入 jinja2 继承的属性，让其他html继承这个父类的html
```
<html>
    <head>
        <meta charset='utf-8'>
        <title>Microblog - {{title}} </title>
        <link href='xxx.css' rel="stylesheet" />>
    </head>
    <body>
        {% block content %}{% endblock %}
    </body>
</html>
```
### index.html
```
{% extends "base.html" %}
{% block content %}
    <h1>Hi, {{ user.username }}</h1>
    {% for post in posts %}
    <div><h2>{{ post.author.username }}</h2><p>Say:{{ post.body }}</p></div>
    {% endfor %}
{% endblock %}

```

### jinja2:
```
{% if xxx %} {% else %} {% endif %}
{% for xxx in xxx %} {% endfor %}
{{ 变量 }}
```

