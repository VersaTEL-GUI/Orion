# coding:utf-8

from mgt_app.show import show_blueprint
from flask import render_template, make_response, jsonify
from mgt_app.utils import read_config


def cors_data(datadict):
    response = make_response(jsonify(datadict))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@show_blueprint.route('/')
def index():
    return render_template("index.html")


@show_blueprint.route('/stor')
def stor():
    return render_template("prompt_show.html")


@show_blueprint.route('/stor/resource')
def resource():
    return render_template("prompt_show.html")


@show_blueprint.route('/stor/resource/show')
def resource_show():
    return render_template("Resource.html")


@show_blueprint.route('/is_master')
def is_master():
    ip_port = read_config.get_master_ip()+':'+read_config.get_web_port()

    return cors_data(ip_port)
