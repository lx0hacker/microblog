from flask import Flask

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

from app import routes,models

