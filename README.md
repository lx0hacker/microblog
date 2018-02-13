# 用户登录
> 用户登录首先要考虑的是用户的密码问题，关于密码安全，最常见的方式是加盐。加盐是为了防止彩虹表攻击，在flask中提供了一个插件Werkzeug供我们使用，个人觉得这让加盐变得没有意义了，因为当黑客盗取了你的数据库，发现是这种格式的密码，同样可以引入flask的插件来暴力破解。下面验证一下
```
from werkzeug.security import generate_password_hash,check_password_hash
hash = generate_password_hash('this$is%secure&password')
print(hash)

password_list = ['qwe123','qwer1234','this$is%secure&password']
for password in password_list:
    flag = check_password_hash(hash,password)
    if flag == True:
        print(password)
```
### 安装flask-login
```
pip install flask-login
```
### 配置
```
__init__.py

from flask_login import LoginManager
login = LoginManager(app)

```
### flask-login
* 提供了四种类型
```
is_authenticated
is_active
is_anonymous
get_id
```
* 提供了一个类供继承 
```
UserMixin
```
* 提供了一个session管理,current_user代表的就是这id返回的User
```
from app import login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

```
* 提供了一个方法用于直接登录用户
login_user(username)

* 提供了一个logout的函数
logout_user(user类，remember='')

* 提供了一个装饰函数用于强制登录
@login_required
> 用法: 当你访问某个需要登陆的页面的时候，会自动跳转到登录页面，同时，网址后缀会带上一个next参数，用于登录后跳转回登录之前的页面。这里会有安全问题，如果没有处理好跳转的网址，会出现客户被挟制到其他网站。因此
```
在__init__.py:

login.login_view ='login'
在需要的地方加上login_required

```
注意：
```
如果显示anonymous没有用户名，那么就是current_user 有错了
如果显示不是is_active的话，那就是login_user的时候错误了
```