# coding:utf-8

from flask import Blueprint

is_master_blueprint = Blueprint("is_master_blueprint", __name__)

from flask_vplx.is_master import views