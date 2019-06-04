#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 13:59
# @Author  : Zhangyp
# @File    : locust_common.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from locust import TaskSet, task, HttpLocust

# from api.serialization import PARA,WEGHT,HOST
# import json
#
# PARA = json.dumps(api_para(10))
# WEGHT = json.dumps(api_weight(10))
# HOST = json.dumps(product_host(10))
PARA = [{"api_id": 20, "api_name": "\u767b\u5f55", "method": "POST", "url": "/Home/Login",
		 "header": {"Content-Type": "application/json"},
		 "body": {"account": "Admin", "password": "888afc9f6809948a9041ba57859b4897", "loginType": "0"},
		 "has_token": True, "pdt_id": 92}]
WEGHT = {"23": [{"api_id": "20", "weight": "1"}]}
HOST = ['http://192.168.1.18:8200']


class TestTask(TaskSet):
	@task(int(WEGHT["23"][0]["weight"]))
	def test_login(self):
		url = HOST[0] + PARA[0]['url']
		# print(url)
		header = {"content-type": "application/json"}
		# header =PARA[0]['header']
		# body = {'account': 'Admin', 'password': '888afc9f6809948a9041ba57859b4897', 'loginType': '0'}
		body = PARA[0]['body']
		name = PARA[0]['api_name']
		response = self.client.post(url, json=body, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()


class TestUser(HttpLocust):
	task_set = TestTask
	min_wait = 1000
	max_wait = 3000
