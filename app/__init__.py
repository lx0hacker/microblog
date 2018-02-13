from flask import Flask
from flask_login import LoginManager

import os
if os.name == 'nt':
    from config import Configqa as Config
else:
    from config import Configcm as Config

#from config import Configqa
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
login.login_view = 'login'
from app import routes,models

