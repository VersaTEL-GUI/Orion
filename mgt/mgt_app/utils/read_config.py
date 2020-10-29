# coding:utf-8

try:
    import configparser as cp
except Exception:
    import ConfigParser as cp


name_of_config_file = 'config.ini'


def read_config_file():
    obj_cfg = cp.ConfigParser(allow_no_value=True)
    obj_cfg.read(name_of_config_file)
    return obj_cfg


class IpPortConfig():

    def __init__(self):
        self.cfg = read_config_file()

    def list_ip(self):
        return list(i[0] for i in self.cfg.items('VPLXIP'))

    def int_port(self):
        return self.cfg.get('VPLXPORT', 'PORT')


if __name__ == '__main__':
    a=IpPortConfig()
    print(a.list_ip(), a.int_port(), type(a.list_ip()))