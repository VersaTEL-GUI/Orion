# coding:utf-8

from flask import jsonify, views, make_response
import sys


sys.path.append('..')

def cors_data(datadict):
    response = make_response(jsonify(datadict))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

class IsMater(views.MethodView):
    def get(self):
        return cors_data(read_flag_file())

def read_flag_file():
    with open('master_flag')as f:
        num = f.read()
    return num
