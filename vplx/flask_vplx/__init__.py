# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data post
'''

from flask import Flask

def create_app():

    from flask_vplx.data import data_blueprint
    from flask_vplx.execution import execution_blueprint
    from flask_vplx.is_master import is_master_blueprint

    app = Flask(__name__)

    # 将蓝图注册到app
    app.register_blueprint(data_blueprint)
    app.register_blueprint(execution_blueprint)
    app.register_blueprint(is_master_blueprint)
    return app
