# coding:utf-8

import urllib3
import os

try:
    import configparser as cp
except Exception:
    import ConfigParser as cp


name_of_config_file = '../../config.ini'


def read_config_file():
    obj_cfg = cp.ConfigParser(allow_no_value=True)
    obj_cfg.read(name_of_config_file)
    return obj_cfg


class IpPortConfig():

    def __init__(self):
        self.cfg = read_config_file()

    def list_ip(self):
        return eval(self.cfg.get('VPLXIP', 'listIP'))

    def int_port(self):
        return self.cfg.get('VPLXPORT', 'PORT')


def get_master_ip():
    cfg = IpPortConfig()
    list_ip, int_port = cfg.list_ip(), cfg.int_port()
    http = urllib3.PoolManager()
    for ip in list_ip:
        str_url = f'http://{ip}:{int_port}/is_master'
        response = http.request('GET', str_url)
        if response.status == 200:
            if "1" in response.data.decode():
                return ip

def get_web_port():
    cfg = IpPortConfig()
    return cfg.int_port()

if __name__ == '__main__':
    a=IpPortConfig()
    print(a.list_ip(), a.int_port(), type(a.list_ip()))