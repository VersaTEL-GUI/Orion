# coding:utf-8

from vplx_app.is_master import is_master_blueprint
from flask import jsonify


def read_flag():
    with open('master_flag')as f:
        r = f.read()
    return r


@is_master_blueprint.route('/is_master')
def is_master():
    return jsonify(read_flag())


if __name__ == '__main__':
    print('aaaa',read_flag())