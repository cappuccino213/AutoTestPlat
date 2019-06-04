#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 9:16
# @Author  : Zhangyp
# @File    : locust_script_gn.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from locust import TaskSet,task,HttpLocust
from script.gn_mssql import random_from_list

class TestTask(TaskSet):
	
	def on_start(self):
		print('test start...')
	
	
	@task
	def test_gn(self):
		api_url='http://192.168.1.18:8920/api/Values/MaxID'
		sCodeConfigID = str(random_from_list())
		url = api_url+'?sCodeConfigID='+sCodeConfigID
		try:
			response = self.client.get(url)
			print(response.status_code)
		except Exception as e:
			print(str(e))
		
		
		
class TestUser(HttpLocust):
	task_set = TestTask
	min_wait = 1000
	max_wait = 2000
	
