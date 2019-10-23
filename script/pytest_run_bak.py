#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 16:10
# @Author  : Zhangyp
# @File    : pytest_run_bak.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""pytest的执行模块"""
import pytest
import os
from py._xmlgen import html
from script.run_parameters import ScriptPara


def get_options(task_id):  # 获取pytest运行参数、记录报告入库、报告复制到templates用于报告访问
	# 报告参数声明
	sp = ScriptPara(task_id)
	project_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
	report_file = 'report_task%s.html' % task_id  # 报告名称
	report = os.path.join(project_path, 'report', report_file)  # 报告路径
	
	# 记录入库
	import time
	report_json = {"report_name": report_file,
				   "task_id": str(task_id),
				   "create_date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
				   "file_path": report}
	from api.controller import report_new_record  # 当存在task_id相同记录，则更新；否则插入记录
	report_new_record(task_id, report_json)
	
	# pytest运行参数（含默认指定html报告参数）
	if sp.data_type() == 'json':
		folder = 'json_script'
	else:
		folder = 'protobuf_script'
	test_dir = os.path.join(project_path, 'script', folder)
	options = ['--html=%s' % report, '--self-contained-html', '--rootdir=%s' % test_dir]  # 生成报告位置,脚本的存放目录
	
	# 将报告html复制到templates
	return options + sp.pytest_option  # 附加配置的参数


def del_script():  # 清理脚本文件，为防止影响下一次的任务执行
	del_path = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'script')  # 遍历路径
	for root, dirs, files in os.walk(del_path):
		for name in files:
			if name.startswith('test_case_') or name.endswith('_pb2.py'):  # 删除测试.py以及当protobuf时的pb2文件
				os.remove(os.path.join(root, name))
				print('接口测试完成，清理执行脚本：%s' % name)


def main(task_id):
	opts = get_options(task_id)
	pytest.main(opts, plugins=[html()])
	del_script()


if __name__ == '__main__':
	main(20)
# del_script()
