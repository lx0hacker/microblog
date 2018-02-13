#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author: lx0hacker
@date:2018-02-07
'''

from app import app,db
from app.models import User,Post

@app.shell_context_processor
def make_shell_context():
    return dict(user=User,post=Post,db=db)