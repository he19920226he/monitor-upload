# -- coding: utf-8 --
import os
import configparser


class Config(object):
    def __init__(self, path=''):
        if path == '':
            path = os.getcwd() + '/config/config.ini'
        self.path = path

    def get_config(self, sections, key, default=''):
        cf = configparser.ConfigParser()
        path_is_exists = os.path.exists(self.path)
        if path_is_exists is False:
            f = open(self.path, 'w')
            f.close()
        cf.read(self.path)
        if not cf.has_section(sections):
            return default

        if not cf.has_option(sections, key):
            return default

        value = cf.get(sections, key)
        if value == '':
            return default

        return value

    def set_config(self, sections, key, value):
        cf = configparser.ConfigParser()
        path_is_exists = os.path.exists(self.path)
        if path_is_exists is False:
            f = open(self.path, 'w')
            f.close()
        cf.read(self.path)
        if not cf.has_section(sections):
            cf.add_section(sections)
        cf.set(sections, key, value)
        with open(self.path, 'w') as f:
            cf.write(f)
