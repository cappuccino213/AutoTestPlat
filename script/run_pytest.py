#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 15:30
# @Author  : Zhangyp
# @File    : run_pytest.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""接口测试（pytest）运行模块"""

import os
project_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) # 项目根目录

def report_record(task_id):
	"""报告记录入库：当存在task_id相同记录，则更新记录；否则插入记录"""
	import time
	report_file = 'report_task%s.html' % task_id  # 报告名称
	report = os.path.join(project_path, 'report', report_file)  # 报告路径
	report_json = {"report_name": report_file,
				   "task_id": str(task_id),
				   "create_date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
				   "file_path": report}
	from api.controller import report_new_record
	report_new_record(task_id, report_json)
	
def pytest_option(task_id):
	"""	pytest的运行参数 """
	from script.run_parameters import ScriptPara
	sp = ScriptPara(task_id)
	if sp.data_type() == 'json':
		folder = 'json_script'
	else:
		folder = 'protobuf_script'
	test_dir = os.path.join(project_path, 'script', folder)
	report = os.path.join(project_path, 'report', 'report_task%s.html' % task_id)
	options = ['--html=%s' % report, '--self-contained-html', '--rootdir=%s' % test_dir] # 默认参数：html报告生成、指明脚本运行目录
	return options + sp.pytest_option

def remove_script():
	"""清理脚本文件，为防止影响下一次的任务执行"""
	remove_path = os.path.join(project_path,'script')
	for root, dirs, files in os.walk(remove_path):
		for name in files:
			if name.startswith('test_case_') or name.endswith('_pb2.py'):  # 删除测试.py以及当protobuf时的pb2文件
				os.remove(os.path.join(root, name))
				print('接口测试完成，清理执行脚本：%s' % name)
				
def report_copy(task_id):
	"""报告复制到templates,便于直接报告访问"""
	import shutil
	src = os.path.join(project_path, 'report', 'report_task%s.html' % task_id) # 报告源
	dst = os.path.join(project_path,'api','templates') # 报告目的
	shutil.copy(src,dst) # 复制一个文件到一个文件或一个目录

def main(task_id):
	import pytest
	from py._xmlgen import html
	opts = pytest_option(task_id)
	pytest.main(opts, plugins=[html()]) # 执行用例
	report_record(task_id)
	remove_script() # 清理脚本
	report_copy(task_id) # 复制report.html

if __name__ == '__main__':
	main(29)
	# print(pytest_option(29))