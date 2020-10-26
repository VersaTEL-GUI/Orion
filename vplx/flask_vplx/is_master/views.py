# coding:utf-8

from flask_vplx.is_master import is_master_blueprint
from flask_vplx.data import model

is_master_blueprint.add_url_rule('/is_master', view_func=model.IsMater.as_view('is_master'))