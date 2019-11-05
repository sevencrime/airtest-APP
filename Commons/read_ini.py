#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser
import os

from Commons.GlobalMap import GlobalMap

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]


def str_to_bool(str):
    '''
    字符串转bool
    :param str:
    :return:
    '''
    return True if str.lower() == 'true' else False

def set_configini(key, newvalue, Section="baseconf"):
    '''
    修改ini文件的数据
    :param key:
    :param newvalue:
    :param Section:
    :return:
    '''
    config.set(Section, key, newvalue)
    config.write(open(rootPath + "pytest.ini", "w"))


config = configparser.ConfigParser()
config.read(rootPath + "pytest.ini")

phone = config.get('baseconf', 'PHONE')

gm = GlobalMap()

gm.set_value(environment=config.get('baseconf', 'environment'))  # 记录数据库
gm.set_bool(isbullion = str_to_bool(config.get('baseconf', 'isbullion')))  # 记录黄金账户是否开启
gm.set_bool(isLeveraged = str_to_bool(config.get('baseconf', 'isLeveraged')))  # 记录外汇账户是否开启
gm.set_value(phone=config.get('baseconf', 'phone'))
gm.set_value(appcationNumber = config.get('baseconf', 'appcationNumber'))
gm.set_value(mongohost = config.get('baseconf', 'mongohost'))



