# -- coding: utf-8 --
import os
import ConfigParser


class Config(object):
    def __init__(self, path=''):
        if path == '':
            path = os.getcwd() + '/config/config.ini'
        self.path = path

    def get_config(self, sections, key, default=''):
        cf = ConfigParser.ConfigParser()
        cf.read(self.path)
        value = cf.get(sections, key)
        if value == '':
            return default
        return value
