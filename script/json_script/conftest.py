#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 15:15
# @Author  : Zhangyp
# @File    : conftest.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import pytest
from datetime import datetime
from py._xmlgen import html

"""
测试报告html配置py，必须放在测试脚本的同级目录下
详细用法可见https://pypi.org/project/pytest-html/
源码：C:\\Users\zhangyp\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\pytest_html\plugin.py
"""


# 编辑报告中的Environment
def pytest_configure(config):
	config._metadata['Test IP'] = '192.168.1.27'


# 编辑Summary
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
	prefix.extend([html.p("QA: zhangyp")])  # 第一行


# summary.extend([html.p("foo: bar")])  #
# postfix.extend([html.p("foo: bar")])  #最后一行


# 编辑报告表头
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):  # cells为list 默认值[outcome(执行结果),test_id,duration,links]
	cells.insert(2, html.th('Description'))  # 描述title放在第3列
	cells.insert(4, html.th('Time', class_='sortable time', col='time'))  # 时间title放在第5列
	cells.pop()  # 删除Links一列


# 编辑报告数据
@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
	cells.insert(2, html.td(report.description))  # 描述value的填写
	cells.insert(4, html.td(datetime.now(), class_='col-time'))  # 时间value的填写
	cells.pop()  # 删除link值一列
	# print(type(report), report)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
	outcome = yield
	report = outcome.get_result()
	report.description = str(item.function.__doc__)
