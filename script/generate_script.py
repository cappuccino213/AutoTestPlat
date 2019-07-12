#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 9:57
# @Author  : Zhangyp
# @File    : generate_script.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

"""
生成locust的执行脚本
1.从api_info数据库获取对应api的数据类型：json or proto
2.根据不同的数据类型，生成对应的脚本json_script()、proto_script()--只是填充的内容有区别、写入文件的函数可以共用
3.若是proto，还需要对proto文件生成对应的对应.py文件
"""
from script.run_parameters import ScriptPara
import os, sys


class GenerateScript():
	def __init__(self, task_id):
		self.task_id = task_id
		self.data_type = self.data_type()
		self.sp = ScriptPara(task_id)
		self.classname = 'case_' + self.sp.case_id[0]  # 脚本的类名
		self.funcname = [i['url'].split('/')[-1].lower() for i in self.sp.para]  # script 函数名
		self.weight = [int(i['weight']) for i in self.sp.weight]  # 执行权重
		self.method = [i['method'].upper() for i in self.sp.para]  # http方法
		self.url = [i + j['url'] for i, j in zip(self.sp.host, self.sp.para)]  # api的请求地址
		self.token = self.sp.token  # 获取token
		for i in self.sp.para:  # 根据是否需要token，将token加入headers
			if i['has_token']:
				i['header']['Authorization'] = self.token
		self.headers = [i['header'] for i in self.sp.para] # 请求头信息
		self.body = [i['body'] for i in self.sp.para] # 请求主体
		self.title = [i['api_name']for i in self.sp.para]  # api测试名称
		self.values = [i['values'] for i in self.sp.para] # 当http为get方法时的值
		self.min = self.sp.min_wait  # locust等待最小值
		self.max = self.sp.max_wait  # locust等待最大值
		
		self.project_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 工程根目录
	
	def data_type(self):  # 判断body的数据类型
		content_type = ScriptPara(self.task_id).para[0]['header']['content-type']
		if 'octet-stream' in content_type:
			return 'proto'
		else:
			return 'json'
	
	def json_script_content(self):  # json类的内容
		code_import = ["from locust import TaskSet, task, HttpLocust"]
		
		code_taskset_class = ["class %sTask(TaskSet):" % self.classname,
						"def on_start(self):",
						"print('start programing...')"]
		code_function = []
		for i in range(len(self.funcname)):
			code_function.append("@task(%d)" % self.weight[i])
			code_function.append("def %s(self):" % self.funcname[i])
			if self.method[i] == 'POST':
				code_function.append("url = '%s'" % self.url[i])
				code_function.append("header = %s" % self.headers[i])
				code_function.append("body = %s" % self.body[i])
				code_function.append("name = '%s'" % self.title[i])
				code_function.append("response = self.client.post(url, json=body, headers=header, name=name)")
				code_function.append("print(response.status_code, response.text)")
				code_function.append("response.raise_for_status()")
			if self.method[i] == 'GET':
				code_function.append("url = '%s%s'" % (self.url[i], self.values[i]))
				code_function.append("header = %s" % self.headers[i])
				code_function.append("name = '%s'" % self.title[i])
				code_function.append("response = self.client.get(url, headers=header, name=name)")
				code_function.append("print(response.status_code, response.text)")
				code_function.append("response.raise_for_status()")
		
		code_httplocust_class = ["class %suser(HttpLocust):" % self.classname,
						   "task_set = %sTask" % self.classname,
						   "min_wait = %d" % self.min,
						   "max_wait = %d" % self.max]
		
		return code_import + code_taskset_class + code_function + code_httplocust_class
	
	def proto_script_content(self):  # proto类脚本的内容
		code_import = ['import sys',
					   'sys.path.append("%s")' % self.project_path,
					   'from locust import TaskSet, task, HttpLocust']
		
		code_taskset_class = ['class %sTask(TaskSet):' % self.classname,
							  'def on_start(self):',
							  'print("start programing...")']
		
		proto_file = [i['proto_file'] for i in self.sp.para]  #
		proto_message = [i['proto_message'] for i in self.sp.para]
		code_function = []
		for i in range(len(self.funcname)):
			code_function.append('@task(%d)' % self.weight[i])
			code_function.append('def %s(self):' % self.funcname[i])
			code_function.append('from script.proto_script.%s_pb2 import %s' % (proto_file[i], proto_message[i]))
			if self.method[i] == 'POST': # 暂时只支持post方法
				code_function.append('url = "%s"' % self.url[i])
				code_function.append('header = %s' % self.headers[i])
				code_function.append('body = %s()' % proto_message[i])
				for key in self.body[i].keys():  # 获取para参数 转化成proto的参数赋值
					value = self.body[i][key] # 根据不同的类型赋值
					if isinstance(value,str):
						code_function.append('body.%s = "%s"' % (key, value))
					if isinstance(value,int):
						code_function.append('body.%s = %d' % (key, value))
					if isinstance(value,bool):
						code_function.append('body.%s = %s' % (key, value))
					if isinstance(value,float):
						code_function.append('body.%s = %f' % (key, value))
				code_function.append('data = body.SerializeToString()')
				code_function.append('name = "%s"' % self.title[i])
				code_function.append('response = self.client.post(url, data=data, headers=header, name=name)')
				code_function.append('result = response.text')
				code_function.append('print(response.status_code, result)')
				code_function.append('response.raise_for_status()')
		
		code_httplocust_class = ["class %sUser(HttpLocust):" % self.classname,
								 "task_set = %sTask" % self.classname,
								 "min_wait = %d" % self.min,
								 "max_wait = %d" % self.max]
		
		return code_import + code_taskset_class + code_function + code_httplocust_class
	
	def write_script(self, py_path,code_list):  # 编写脚本
		with open(os.path.join(py_path,self.classname + '.py'), 'w+', encoding='UTF-8') as py_file:
			for code_line in code_list:
				if str(code_line).startswith('import') or str(code_line).startswith('from locust') or str(
						code_line).startswith('sys.path'):
					py_file.write(str(code_line) + '\n')
				elif str(code_line).startswith('class'):
					py_file.write('\n' + str(code_line) + '\n')
				elif str(code_line).startswith('@'):
					py_file.write('\n' + '\t' + str(code_line))
				elif str(code_line).startswith('def'):
					py_file.write('\n' + '\t' + str(code_line) + '\n')
				elif str(code_line).startswith('task_set =') or str(code_line).startswith('min_wait =') or str(
						code_line).startswith('max_wait ='):
					py_file.write('\t' + str(code_line) + '\n')
				else:
					py_file.write('\t\t' + str(code_line) + '\n')
	
	def proto2py(self):  # 将proto编译生成py文件
		import subprocess
		proto_file = [i['proto_file'] + '.proto' for i in self.sp.para]  # proto文件名
		proto_path = os.path.join(self.project_path, 'api', 'static', 'proto_file')  # proto文件目录
		py_path = os.path.join(self.project_path, 'script', 'proto_script')  # 编译生成py文件目录
		proto_list = [os.path.join(proto_path, proto) for proto in proto_file]  # proto文件路径
		for proto in proto_list:
			cli = "protoc -I=%s --python_out=%s %s" % (proto_path, py_path, proto)  # 编译proto生成py文件
			subprocess.Popen(cli, stdout=subprocess.PIPE, shell=True)
	
	def main(self):  # 执行生成脚本
		if self.data_type == 'json':
			py_path = os.path.join(self.project_path,'script','json_script')
			self.write_script(py_path,self.json_script_content())
		elif self.data_type == 'proto':
			py_path = os.path.join(self.project_path,'script','proto_script')
			self.proto2py()
			self.write_script(py_path,self.proto_script_content())
		else:
			print('Other formats are not supported except json and proto')


if __name__ == '__main__':
	g = GenerateScript(15)
	# g.proto_script_content()
	# g.write_script(r'D:\flask-project\ApiPerformanceTest\script\proto_script',g.proto_script_content())
	g.main()
