#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author: lx0hacker
@date:2018-02-07
'''

from app import create_app,db
from flask_migrate import Migrate,upgrade
from app.models import User,Role
import click

app = create_app('default')
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell():
    return dict(db=db,User=User,Role=Role)


@app.cli.command()
def deploy():
    upgrade()
    Role.insert_roles()

