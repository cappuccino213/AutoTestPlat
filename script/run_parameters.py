#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 11:15
# @Author  : Zhangyp
# @File    : run_parameters.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from api.controller import  task_select_id,case_select_id,api_select_id,pdt_select_id
from appconfig.read_ini import TOKENSEVER,MINWAIT,MAXWAIT
class ScriptPara(object):
	"""
	根据任务id获取生成脚本所需要的参数
	"""
	def __init__(self,task_id):
		self.task_id = task_id
		self.option = self.locust_option() #locust_cl命令参数
		self.locust_url = self.locust_url()
		self.case_id = self.get_id() # 根据任务id获取case的id
		self.weight = self.api_weight() # 根据任务id获取api的权值
		self.para = self.api_para() # 根据任务id获取api的参数列表
		self.host = self.pdt_host() # 根据任务id获取产品host
		self.token = self.get_token() # 获取token
		self.min_wait = int(MINWAIT)
		self.max_wait = int(MAXWAIT)
		
	def locust_option(self):
		cl_list = task_select_id(self.task_id)['locust_cl']
		cl = [i['parameter'] for i in cl_list if i['need']==1] # 获取need=1的选项
		# 获取need=1的选项
		# for i in range(len(cl_list)):
		# 	if cl_list[i]['need'] == 1:
		# 		cl.append(cl_list[i]['parameter'])
		option = " ".join(cl)
		return option
	
	def get_id(self):
		case = task_select_id(self.task_id)['associated_case']
		case_list = [case['case_id'] for case in case] # 列表推导方式获取case_id
		return case_list
	
	def api_weight(self):
		weight = [case_select_id(case_id)['api_weight'] for case_id in self.case_id]
		weight_list = [j for i in weight for j in i] #剥离二维数组
		return weight_list
	
	def api_para(self):
		aid = [j['api_id'] for j in self.weight]
		para = [api_select_id(i) for i in aid]
		return para
	
	def pdt_host(self):
		pid = [i["pdt_id"] for i in self.para]
		pdt = [pdt_select_id(i) for i in pid]
		p_host = [i["host"] for i in pdt]
		return p_host
	
	def get_token(self):
		import requests
		url = TOKENSEVER
		headers = {'Content-Type': 'application/json'}
		body = {"UniqueIdentity":"zyp",
				"Audience":"eWordPOD",
				"CustomData":"",
				"Expire":960} #token的时效性默认设置为8个小时，为什么脚本token的时效性考虑
		response = requests.post(url,headers=headers,json=body)
		return response.json()['token']
	
	def locust_url(self):
		import re
		temp = self.option
		#找到host
		find_host=r'--web-host=.{12}'
		host_exp = re.findall(re.compile(find_host),temp)[0]
		host = re.sub('--web-host=','',host_exp)
		#找到端口
		find_port=r'--web-port=.{4}' #注意这里设置了4位的端口号
		port_exp = re.findall(re.compile(find_port),temp)[0]
		port = re.sub('--web-port=','',port_exp)
		url = host+':'+port
		return url
	
if __name__=="__main__":
	sp = ScriptPara(10)
	# print(sp.weight)
	# print(sp.option)
	# print(sp.case_id)
	# print(sp.para)
	# print(sp.host)
	print(sp.api_para())