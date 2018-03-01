#!/usr/bin/env python
#-*- cdoing;utf-8 -*-

from flask import render_template
from . import main
from .. import db
from ..models import User

@main.route('/')
def index():
    return render_template('main/index.html',title='index')

