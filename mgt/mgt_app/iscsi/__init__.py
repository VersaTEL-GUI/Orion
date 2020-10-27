# coding:utf-8

'''
Created on 2020/3/2
@author: Paul
@note: data
'''

from flask import Blueprint

iscsi_blueprint = Blueprint("iscsi_blueprint", __name__,template_folder='templates')

from mgt_app.iscsi import views