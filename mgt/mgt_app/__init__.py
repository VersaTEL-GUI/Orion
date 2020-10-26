# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data post
'''

from flask import Flask
from mgt_app.utils import read_config as gc


def create_app():
    
    app = Flask(__name__)

    # 将蓝图注册到app
    from mgt_app.show import show_blueprint
    from mgt_app.config import config_blueprint
    app.register_blueprint(show_blueprint, url_prefix="")
    app.register_blueprint(config_blueprint, url_prefix="")
    return app



