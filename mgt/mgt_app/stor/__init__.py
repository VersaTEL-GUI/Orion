# coding:utf-8

'''
Created on 2020/3/2
@author: Paul
@note: data
'''

from flask import Blueprint

stor_blueprint = Blueprint("stor_blueprint", __name__,template_folder='templates')

<<<<<<< HEAD:mgt/mgt_app/show/__init__.py
from mgt_app.show import stor_resource



# 捕获404异常错误
@app.errorhandler(404)
# 当发生404错误时，会被该路由匹配
def handle_404_error(err_msg):
    """自定义的异常处理函数"""
    # 这个函数的返回值就是前端用户看到的最终结果 (404错误页面)
    return u"出现了404错误， 错误信息：%s" % err_msg
=======
from mgt_app.stor import views
>>>>>>> 29bfbb7fad6b8638ae0ddea91efdf0355e2c758b:mgt/mgt_app/stor/__init__.py
