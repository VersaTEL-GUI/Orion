# coding:utf-8

from mgt_app.config import config_blueprint
from flask import render_template


@config_blueprint.route('/')
def index():
    return render_template("index.html")


@config_blueprint.route('/iscsi')
def iscsi():
    return render_template("prompt_create.html")


@config_blueprint.route('/iscsi/map')
def iscsi_map():
    return render_template("prompt_create.html")


@config_blueprint.route('/iscsi/map/create')
def map_create():
    return render_template("iSCSI_create.html")