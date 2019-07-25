#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 16:10
# @Author  : Zhangyp
# @File    : pytest_run.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""pytest的执行模块"""
import pytest
import os
from py._xmlgen import html
from script.run_parameters import ScriptPara

def get_options(task_id):
	sp = ScriptPara(task_id)
	project_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
	report_file = 'report_task%s.html'%task_id
	report = os.path.join(project_path,'report',report_file)
	if sp.data_type()=='json':
		folder = 'json_script'
	else:
		folder = 'protobuf_script'
	test_dir = os.path.join(project_path,'script',folder)
	options = ['--html=%s' % report,'--rootdir=%s'%test_dir]  # 生成报告位置,脚本的存放目录
	return options+sp.pytest_option # 附加配置的参数

def main(task_id):
	opts = get_options(task_id)
	pytest.main(opts, plugins=[html()])

if __name__=='__main__':
	main(20)