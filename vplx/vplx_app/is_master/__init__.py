# coding:utf-8

from flask import Blueprint

is_master_blueprint = Blueprint("is_master_blueprint", __name__)

from vplx_app.is_master import read_flag