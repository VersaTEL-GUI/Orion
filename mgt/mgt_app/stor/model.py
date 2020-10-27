
# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data
'''

from flask import render_template, views, jsonify
from ..utils import conn_vplx as cv

class Index(views.MethodView):
    def get(self):
        return render_template("index.html")
    
class Stor(views.MethodView):
    def get(self):
        return render_template("prompt_show.html")

class IsMaster(views.MethodView):
    def get(self):
        is_master = {
            'is_master_ip' :cv.get_master_ip()+":"+cv.get_web_port()
        }
        return jsonify(is_master)
    
class Resource(views.MethodView):
    def get(self):
        return render_template("Resource.html")
