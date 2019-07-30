# -- coding: utf-8 --
import os
import configparser
import time


class Config(object):
    def __init__(self, path=''):
        if path == '':
            path = os.getcwd() + '/config/config.ini'
        self.path = path

    def get_config(self, sections, key, default=''):
        cf = configparser.ConfigParser()
        path_is_exists = os.path.exists(self.path)
        if path_is_exists is False:
            print('config file error..............')
            time.sleep(5)
            exit()
        value = ''
        try:
            cf.read(self.path)
            value = cf.get(sections, key)
        except ConfigParser.DuplicateSectionError:
            print('sections:' + sections + ' is error')
            time.sleep(5)
            exit()
        if value == '':
            return default
        return value
