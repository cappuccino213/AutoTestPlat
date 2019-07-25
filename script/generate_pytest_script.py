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
		script_file = os.path.join(self.script_path('json'), self.script_file[0])
		self.generate_script(script_file + '.py', self.json_script_content()[0], self.json_script_content()[1])


if __name__ == '__main__':
	s = PytestScript(20)
	s.main()
# print(s.verify_expection)
# print(s.script_funcname)
