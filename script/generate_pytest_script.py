#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 16:08
# @Author  : Zhangyp
# @File    : generate_pytest_script.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""
pytest根据数据生成对应的测试脚本
"""
import os
import time
from script.run_parameters import ScriptPara


class PytestScript(object):
	def __init__(self, task_id):
		"""定义脚本生成需要用到的参数"""
		self.task_id = task_id
		self.script_para = ScriptPara(task_id)  # 脚本参数源
		self.api_url = [i + j['url'] for i, j in zip(self.script_para.host, self.script_para.para)]
		self.api_method = [i['method'].upper() for i in self.script_para.para]
		self.api_token = self.script_para.token
		for i in self.script_para.para:  # 根据是否需要token，将token加入headers
			if i['has_token']:
				i['header']['Authorization'] = self.api_token
		self.api_headers = [self.dictvalue2str(i['header']) for i in self.script_para.para]
		self.api_data = [i['body'] for i in self.script_para.para]
		self.api_values = [i['values'] for i in self.script_para.para]  # 当http为get方法时的值
		self.verify_expection = [i['expection'] for i in self.script_para.api_expection]  # 期望结果，用于检验接口正确性json格式
		# if not self.verify_expection:
		self.script_funcname = ['test_' + i['url'].split('/')[-1].lower() for i in self.script_para.para]  # script 函数名
		self.script_funcname = list(self.rename_duplicates(self.script_funcname))
		self.script_file = ['test_case_' + case_id for case_id in self.script_para.case_id]  # 根据case_id命名脚本名字
		self.project_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 工程根目录
		self.generate_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
		self.options = self.script_para.pytest_option # pytest运行参数
	
	def script_path(self, protocol):  # 根据协议类型获取脚本路径
		if protocol == 'json':
			return os.path.join(self.project_path, 'script', 'json_script')
		else:
			return os.path.join(self.project_path, 'script', 'protobuf_script')
	
	def dictvalue2str(self, dictionary):  # 处理header里面的嵌套dict，转化成str
		di = {}
		for key, value in dictionary.items():
			if isinstance(value, dict):
				value = str(value)
			di[key] = value
		return di
	
	def rename_duplicates(self, old):  # 将列表中重复项以附加计数方式重命名
		seen = {}
		for x in old:
			if x in seen:
				seen[x] += 1
				yield "%s_%d" % (x, seen[x])
			else:
				seen[x] = 0
				yield x
				
	def data_type(self):  # 判断body的数据类型
		content_type = ScriptPara(self.task_id).para[0]['header']['content-type']
		if 'octet-stream' in content_type:
			return 'protobuf'
		else:
			return 'json'
	
	def json_script_content(self):
		code_comments = """# -*- coding: utf-8 -*-
# generate time:%s
""" % self.generate_time
		code_import = """import requests"""
		
		code_verify = """def verify(res,expection):
	if res.status_code == expection['status_code']:
		return True
	else:
		return False
		"""
		
		code_test_api = []  # 测试api的函数
		for i in range(len(self.script_funcname)):
			code_test_api.append("def %s():" % self.script_funcname[i])
			code_test_api.append("headers = %s" % self.api_headers[i])
			code_test_api.append("expection = %s" % self.verify_expection[i])
			if self.api_method[i] == 'GET':
				code_test_api.append("data = None")
				code_test_api.append("url = '%s%s'" % (self.api_url[i], self.api_values[i]))
			if self.api_method[i] == 'POST':
				code_test_api.append("data = %s" % self.api_data)
				code_test_api.append("url = '%s'" % self.api_url[i])
			code_test_api.append(
				"res = requests.request(method='%s',url=url,data=data,headers=headers)" % self.api_method[i])
			code_test_api.append("assert verify(res,expection)")
		
		# code_run = ["def main():"]
		# code_run.append("pytest.main(%s, plugins=%s)" % (self.options['options'], self.options['plugins']))  # 执行pytest的函数
		
		return code_comments + '\n\n' + code_import + '\n\n' + code_verify, code_test_api
	
	def protobuf_script_content(self):
		code_comments = """# -*- coding: utf-8 -*-
# generate time:%s
""" % self.generate_time
		code_import = """import requests"""
		
		code_verify = """def verify(res,expection):
	if res.status_code == expection['status_code']:
		return True
	else:
		return False
		"""
		protobuf_file = [i['proto_file'] for i in self.script_para.para]
		protobuf_message = [i['proto_message'] for i in self.script_para.para]
		code_test_api = []
		for i in range(len(self.script_funcname)):
			code_test_api.append("def %s():" % self.script_funcname[i])
			code_test_api.append("headers = %s" % self.api_headers[i])
			code_test_api.append("expection = %s" % self.verify_expection[i])
			if self.api_method[i]=='POST':
				code_test_api.append('from script.protobuf_script.%s_pb2 import %s' % (protobuf_file[i], protobuf_message[i]))
				code_test_api.append('url = "%s"' % self.api_url[i])
				code_test_api.append('data = %s()' % protobuf_message[i])
				for key in self.api_data[i].keys(): # 根据不同的类型赋值
					value = self.api_data[i][key]
					if isinstance(value, str):
						code_test_api.append('data.%s = "%s"' % (key, value))
					if isinstance(value, int):
						code_test_api.append('data.%s = %d' % (key, value))
					if isinstance(value, bool):
						code_test_api.append('data.%s = %s' % (key, value))
					if isinstance(value, float):
						code_test_api.append('data.%s = %f' % (key, value))
				code_test_api.append('data = data.SerializeToString()')
				code_test_api.append('res = requests.request(method="POST", url=url, data=data, headers=headers)')
			else:
				code_test_api.append("url = '%s%s'" % (self.api_url[i], self.api_values[i]))
				code_test_api.append("data = None")
				code_test_api.append('res = requests.request(method="GET", url=url, data=data, headers=headers)')
			code_test_api.append("assert verify(res, expection)")
		return code_comments + '\n\n' + code_import + '\n\n' + code_verify, code_test_api
	
	def proto2py(self):  # 将proto编译生成py文件
		import subprocess
		proto_file = [i['proto_file'] + '.proto' for i in self.script_para.para]  # proto文件名
		proto_path = os.path.join(self.project_path, 'api', 'static', 'proto_file')  # proto文件目录
		py_path = os.path.join(self.project_path, 'script', 'protobuf_script')  # 编译生成py文件目录
		proto_list = [os.path.join(proto_path, proto) for proto in proto_file]  # proto文件路径
		for proto in proto_list:
			if self.if_proto_import(proto):
				cli = "protoc -I=%s --python_out=%s %s --include_imports %s" % (
					proto_path, py_path, proto, self.if_proto_import(proto))
			else:
				cli = "protoc -I=%s --python_out=%s %s" % (proto_path, py_path, proto)
			subprocess.Popen(cli, stdout=subprocess.PIPE, shell=True)  # 编译proto生成py文件
	
	def if_proto_import(self, proto):  # 判断proto中是否又依赖其他proto导入
		import codecs, re
		with codecs.open(proto, 'r', encoding='utf-8', errors='ignore') as f:
			data = f.readlines()
			for line in data:
				if "import" in line:
					import_proto = re.findall('.*"(.*)".*', line)  # 取引号中的proto名列表
					return "".join(import_proto)  # 返回proto名

	
	def generate_script(self, script_file, code_static, code_dynamic):
		"""
		:param script_file: 脚本文件
		:param code_static: 脚本中固定不变的内容，用带格式的字符串填入
		:param code_dynamic:脚本中根据入参变化的内容，list按照规则填入
		"""
		with open(script_file, 'w+', encoding='UTF-8') as script:
			script.write(code_static)  # 先写入固定的代码
			for code_line in code_dynamic:
				if str(code_line).startswith('def'):
					script.write('\n\n' + str(code_line) + '\n')
				else:
					script.write('\t' + str(code_line) + '\n')
	
	def main(self):# 执行生成脚本
		if self.data_type() == 'json':
			script_file = os.path.join(self.script_path('json'),
									   self.script_file[0])  # 暂时只支持一个case，多个case支持需要遍历此处的script列表
			self.generate_script(script_file + '.py', self.json_script_content()[0], self.json_script_content()[1])
		elif self.data_type() == 'protobuf':
			script_file = os.path.join(self.script_path('protobuf'),
									   self.script_file[0])  # 暂时只支持一个case，多个case支持需要遍历此处的script列表
			self.proto2py()
			self.generate_script(script_file + '.py', self.protobuf_script_content()[0], self.protobuf_script_content()[1])
		else:
			print('Other formats are not supported except json and proto')
			

if __name__ == '__main__':
	s = PytestScript(29)
	s.main()
# print(s.verify_expection)
# print(s.script_funcname)
