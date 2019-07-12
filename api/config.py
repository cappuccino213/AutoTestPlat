#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 17:38
# @Author  : Zhangyp
# @File    : config.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from appconfig.read_ini import CONF

SQLALCHEMY_DATABASE_URI = CONF['connect_string']
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# api.config['SQLALCHEMY_DATABASE_URI'] = get_conf()['connect_string']
# api.config['SQLALCHEMY_ECHO'] = True  # 如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
# api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存，
# # 如果不必要的可以禁用它。

