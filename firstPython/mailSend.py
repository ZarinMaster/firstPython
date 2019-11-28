# -*- coding: utf-8 -*-
# @Time : 2019/11/26 16:07
# @Author : ZarinMaster
# @Site : 
# @File : mailSend.py
# @Software: PyCharm

import time

import yaml


class emailClass(object):
    # __slots__ = ('_sender', '_receivers')

    def __init__(self):
        self.currentTime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        yaml.load(open('.res/mailConfig.yaml'))
