#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 16:58
# @Author  : Zhangyp
# @File    : read_ini.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import os
import logging
import codecs
from logging import handlers
import configparser


# 判断路径是否存在，不存在，则在当前目录下自动创建
def exits_path(dir_path):
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
	# print('make successfully')
	return dir_path


# 删除windows文本中utf8的BOM
def remove_bom(file_path):
	with open(file_path, 'r+b') as file:
		data = file.read(3)
		if data == codecs.BOM_UTF8:  # 判断首字符是否为UTF8的BOM
			content = file.read()
			file.seek(0)
			file.write(content)
			file.truncate()


# 定义一个日志类
class Logger(object):
	level_mappings = {
		'debug': logging.DEBUG,
		'info': logging.INFO,
		'warning': logging.WARNING,
		'error': logging.ERROR,
		'critical': logging.CRITICAL
	}
	
	def __init__(self, filename, level='error', when='D', back_count=3, fmt='''[时间]:%(asctime)s
[线程]:%(thread)s
[级别]:%(levelname)s
[路径]:%(pathname)s
[函数]:%(funcName)s
[行号]:%(lineno)d
[信息]:%(message)s
------------------
	'''):
		self.logger = logging.getLogger(filename)  # set record log as file with name
		self.logger.setLevel(self.level_mappings.get(level))  # set log level
		format_str = logging.Formatter(fmt)  # set the log format
		sh = logging.StreamHandler()  # output to console
		sh.setFormatter(format_str)  # log format of console
		th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=back_count, encoding='utf-8')
		th.setFormatter(format_str)  # log format of file
		self.logger.addHandler(sh)  # 把对象加到logger里面
		self.logger.addHandler(th)


# 读取配置文件，以key:value形式返回
def get_conf():
	cur_path = os.path.abspath(os.path.dirname(__file__))
	log_path = os.path.join(exits_path(os.path.join(cur_path,'log')),'read_ini.log')
	log = Logger(log_path, level='error') # 调式时日志改成info
	ini_path = os.path.join(cur_path,'appsettings.ini')
	try:
		cf = configparser.ConfigParser()
		remove_bom(ini_path)
		cf.read(ini_path, encoding='utf-8')
		section = cf.sections()
		kv = []
		for i in range(len(section)):
			kv = kv + cf.items(section[i])
		s = dict((x, y) for x, y in kv)  # 将tuple转化成dic
		log.logger.info('read ini:%s' % s)
		return s
	except Exception as e:
		log.logger.error(str(e))


CONF = get_conf()
TOKENSEVER = CONF['token_server']
MINWAIT = CONF['min_wait']
MAXWAIT = CONF['max_wait']
CLIENTPATH = CONF['path']


if __name__ == '__main__':
	print(CONF)
