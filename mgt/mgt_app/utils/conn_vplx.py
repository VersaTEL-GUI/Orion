#coding:utf-8

import urllib3
from .read_config import IpPortConfig


def get_master_ip():
    cfg = IpPortConfig()
    list_ip, int_port = cfg.list_ip(), cfg.int_port()
    http = urllib3.PoolManager()
    for ip in list_ip:
        str_url = f'http://{ip}:{int_port}/is_master'
        try:
            response = http.request('GET', str_url)
            if response.status == 200:
                if "1" in response.data.decode():
                    return ip
        except:
            return ip


def get_web_port():
    cfg = IpPortConfig()
    return cfg.int_port()
