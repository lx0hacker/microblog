# web 表单
> 分离原则，将配置文件单独分离出来，以确保后期比较好修改。
创建config.py
```
import os
class Config(object):
    SECRET_KEY = 'qwer1234'

```
为什么要有secret key？
这是为了防止CSRF攻击，在每个表单中植入一个随机值，随着客户端发送到服务器端进行解密验证。当然最安全的做法是写在环境变量里面。
# __init__.py
在__init__.py里面引入配置。也就是在实例上绑定配置
```
...
app.config.from_object(Config)
...

```
# 开始使用web表单
* 具体分为三步
1. 新建对象
2. ruote引用
3. 新建html渲染

* 注意事项
1. 每个html表单里面都必须要有csrf token form.hidden_tag()
2. 当运行validate_on_submit()这个方法，就会收集所有的validate_xxx(表的字段名)，执行

* 规划
1. 登录： 用户名，密码，记住我，登录按钮
2. 注册： 用户名，密码，密码2，邮箱，注册按钮

# index.html 新增登录入口
```
...
{% if user.username %}
<h1>Hi, {{ user.username }}</h1>
<p><a href="#">logout</a></p>
{% else %}
<h1>Hi, Anonmous</h1>
<p><a href="{{url_for('login')}}">Login</a></p>
{% endif %}
...
```
# forms.py
```
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username: ',validators=[DataRequired()])
    password = PasswordField('Password: ',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')
```

