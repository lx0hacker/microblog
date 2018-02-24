#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author: lx0hacker
@date:2018-02-07
'''

from app import create_app,db
from flask_migrate import Migrate
from app.models import User,Role

app = create_app('default')
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell():
    return dict(db=db,User=User,Role=Role)