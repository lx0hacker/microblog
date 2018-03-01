#!/usr/bin/env python
#coding:utf-8
'''
    @Author:John Wen
    @description:
        
'''
from . import admin
from ..decorators import admin_required,permission_required
from ..models import Permission
from flask_login import login_required

@admin.route('/admin')
@login_required
@admin_required
def for_admin_only():
    return "For administrators"

@admin.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "For Moderator comments!"

@admin.route('/user')
@login_required
@permission_required(Permission.WRITE_ARTICLE)
def for_user_only():
    return "For User"

