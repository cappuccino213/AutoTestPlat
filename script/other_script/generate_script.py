#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 16:10
# @Author  : Zhangyp
# @File    : generate_script.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from script.generate_script import package_code,TaskSet_code,function_code,HttpLocust_code
from script.generate_script import CLASSNAME


def generate_script():
	"""
	自动生成脚本
	"""
	with open('%s.py'%CLASSNAME, 'w+', encoding='UTF-8') as w:
		for i in package_code:
			w.write(str(i)+'\n')
		for i in TaskSet_code:
			if i.startswith('class'):
				w.write(str(i)+'\n')
			elif i.startswith('def'):
				w.write('\n'+'\t'+str(i)+'\n')
			else:
				w.write('\t\t'+str(i)+'\n')
		for i in function_code:
			if i.startswith('class'):
				w.write(str(i)+'\n')
			elif i.startswith('@'):
				w.write('\n'+'\t'+str(i))
			elif i.startswith('def'):
				w.write('\n'+'\t'+str(i)+'\n')
			else:
				w.write('\t\t'+str(i)+'\n')
		for i in HttpLocust_code:
			if i.startswith('class'):
				w.write('\n'+str(i)+'\n')
			else:
				w.write('\t'+str(i)+'\n')
				
if __name__=='__main__':
	generate_script()