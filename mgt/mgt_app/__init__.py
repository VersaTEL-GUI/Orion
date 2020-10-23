# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data post
'''

from flask import Flask
from mgt_app import get_config as gc
import urllib3


def create_app():
    
    app = Flask(__name__)

    # 将蓝图注册到app
    from mgt_app.show import show_blueprint
    from mgt_app.config import config_blueprint
    app.register_blueprint(show_blueprint)
    app.register_blueprint(config_blueprint)
    return app

def get_master_ip():
    cfg = gc.IpPortConfig()
    list_ip, int_port = cfg.list_ip(), cfg.int_port()
    http = urllib3.PoolManager()
    for ip in list_ip:
        str_url = f'http://{ip}:{int_port}/is_master'
        response = http.request('GET', str_url)
        if response.status == 200:
            if "1" in response.data.decode():
                return ip
