#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 14:04
# @Author  : Zhangyp
# @File    : controller.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import platform, subprocess
from api.modles import *
import os, json


# product相关操作
def pdt_select():
	products = Product.query.filter(Product.delete_flag != 1).all()
	pl = []
	for i in range(len(products)):
		to_json = {
			'pdt_id': products[i].pdt_id,
			'pdt_name': products[i].pdt_name,
			'version': products[i].version,
			'description': products[i].description,
			'host': products[i].host,
			'api_json': products[i].api_json
		}
		pl.append(to_json)
	return pl


def pdt_select_id(pdt_id):
	try:
		result = Product.query.get(pdt_id)
		to_json = {
			'pdt_id': result.pdt_id,
			'pdt_name': result.pdt_name,
			'version': result.version,
			'description': result.description,
			'host': result.host,
			'api_json': result.api_json
		}
		return to_json
	except Exception as e:
		return {"desc": "暂未查询到数据,原因：%s" % str(e)}


def pdt_insert(post_json):
	pro = Product(pdt_name=post_json['pdt_name'], version=post_json['version'], description=post_json['description'],
				  host=post_json['host'], api_json=post_json['api_json'])
	db.session.add(pro)
	db.session.commit()


def pdt_update(put_json):
	result = Product.query.get(put_json['pdt_id'])  # 通过主键查询
	result.pdt_name = put_json['pdt_name']
	result.version = put_json['version']
	result.host = put_json['host']
	result.description = put_json['description']
	result.api_json = put_json['api_json']
	db.session.commit()


def pdt_update_api_json(put_json):  # 更新api_json
	result = Product.query.get(put_json['pdt_id'])
	result.api_json = put_json['api_json']
	db.session.commit()


def pdt_delete(del_json):
	result = Product.query.filter_by(pdt_id=del_json['pdt_id']).first()
	result.delete_flag = True
	# db.session.delete(result)
	db.session.commit()


# 	API相关操作
def api_select():
	apis = ApiInfo.query.all()
	al = []
	for i in range(len(apis)):
		to_json = {'api_id': apis[i].api_id,
				   'api_name': apis[i].api_name,
				   'method': apis[i].method,
				   'url': apis[i].url,
				   'header': apis[i].header,
				   'body': apis[i].body, 'has_token': apis[i].has_token,
				   'pdt_id': apis[i].pdt_id,
				   'pdt_name': pdt_select_id(apis[i].pdt_id)['pdt_name'],
				   'values': apis[i].values,
				   'proto_message': apis[i].proto_message,
				   'proto_file': apis[i].proto_file}
		al.append(to_json)
	return al


def api_select_id(api_id):
	try:
		result = ApiInfo.query.get(api_id)
		to_json = {
			'api_id': result.api_id,
			'api_name': result.api_name,
			'method': result.method,
			'url': result.url,
			'header': result.header,
			'body': result.body,
			'has_token': result.has_token,
			'pdt_id': result.pdt_id,
			'values': result.values,
			'proto_message': result.proto_message,
			'proto_file': result.proto_file
		}
		return to_json
	except Exception as e:
		return {"desc": "暂未查询到数据,原因：%s" % str(e)}


def api_select_filter(pdt_id):
	try:
		result = ApiInfo.query.filter_by(pdt_id=pdt_id).all()
		al = []
		for i in range(len(result)):
			to_json = {
				'api_id': result[i].api_id,
				'api_name': result[i].api_name,
				'method': result[i].method,
				'url': result[i].url,
				'header': result[i].header,
				'body': result[i].body,
				'has_token': result[i].has_token,
				'pdt_id': result[i].pdt_id,
				'values': result[i].values,
				'proto_message': result[i].proto_message,
				'proto_file': result[i].proto_file
			}
			al.append(to_json)
		return al
	except Exception as e:
		return {"desc": "暂未查询到数据,原因：%s" % str(e)}


def api_insert(post_json):
	api = ApiInfo(api_name=post_json['api_name'],
				  method=post_json['method'],
				  url=post_json['url'],
				  header=post_json['header'],
				  body=post_json['body'],
				  has_token=post_json['has_token'],
				  pdt_id=post_json['pdt_id'],
				  values=post_json['values'],
				  proto_message=post_json['proto_message'],
				  proto_file=post_json['proto_file'])
	db.session.add(api)
	db.session.commit()


def api_update(put_json):
	result = ApiInfo.query.get(put_json['api_id'])
	result.api_name = put_json['api_name']
	result.method = put_json['method']
	result.url = put_json['url']
	result.header = put_json['header']
	result.body = put_json['body']
	result.has_token = put_json['has_token']
	result.pdt_id = put_json['pdt_id']
	result.values = put_json['values']
	result.proto_message = put_json['proto_message']
	result.proto_file = put_json['proto_file']
	db.session.commit()


def api_delete(del_json):
	result = ApiInfo.query.filter_by(api_id=del_json['api_id']).first()
	db.session.delete(result)
	db.session.commit()


# case相关操作
def case_select():
	cases = CaseInfo.query.all()
	cl = []
	for i in range(len(cases)):
		to_json = {'case_id': cases[i].case_id,
				   'case_name': cases[i].case_name,
				   'api_weight': cases[i].api_weight,
				   'type_id': cases[i].type_id,
				   'api_expection': cases[i].api_expection,
				   'associated_pdt_id': cases[i].associated_pdt_id}
		cl.append(to_json)
	return cl


def case_select_id(case_id):
	try:
		result = CaseInfo.query.get(case_id)
		to_json = {
			'case_id': result.case_id,
			'case_name': result.case_name,
			'api_weight': result.api_weight,
			'type_id': result.type_id,
			'api_expection': result.api_expection,
			'associated_pdt_id': result.associated_pdt_id
		}
		return to_json
	except Exception as e:
		return {"desc": "暂未查询到数据,原因：%s" % str(e)}


def case_insert(post_json):
	case = CaseInfo(case_name=post_json['case_name'],
					api_weight=post_json['api_weight'],
					type_id=post_json['type_id'],
					api_expection=post_json['api_expection'],
					associated_pdt_id=post_json['associated_pdt_id']
					)
	db.session.add(case)
	db.session.commit()


def case_update(type_id, put_json):
	result = CaseInfo.query.get(put_json['case_id'])
	result.case_name = put_json['case_name']
	result.type_id = put_json['type_id']
	result.associated_pdt_id = put_json['associated_pdt_id']
	if type_id == 1:
		result.api_weight = put_json['api_weight']
	elif type_id == 2:
		result.api_expection = put_json['api_expection']
	else:
		pass
	db.session.commit()


def case_delete(del_json):
	result = CaseInfo.query.get(del_json['case_id'])
	db.session.delete(result)
	db.session.commit()


# task相关操作
def task_select():
	tasks = TaskInfo.query.all()
	tl = []
	for i in range(len(tasks)):
		to_json = {'task_id': tasks[i].task_id,
				   'task_name': tasks[i].task_name,
				   'associated_case': tasks[i].associated_case,
				   'task_status': tasks[i].task_status,
				   'locust_cl': tasks[i].locust_cl,
				   'pytest_para': tasks[i].pytest_para}
		tl.append(to_json)
	return tl


def task_mlist():  # 任务列表显示内容
	tasks = task_select()
	for task in tasks:
		try:  # 脏数据处理，当case表、task表不同时删除时的异常数据
			task['type_id'] = case_select_id(task['associated_case'][0]['case_id'])['type_id']
		except:
			task['type_id'] = None
		if task['type_id'] == 1:
			task['parameter'] = task['locust_cl']
		elif task['type_id'] == 2:
			task['parameter'] = task['pytest_para']
		else:
			task['parameter'] = []
		del task['locust_cl']
		del task['pytest_para']
	return tasks


def task_select_id(task_id):
	try:
		result = TaskInfo.query.get(task_id)
		to_json = {
			'task_id': result.task_id,
			'task_name': result.task_name,
			'associated_case': result.associated_case,
			'task_status': result.task_status,
			'locust_cl': result.locust_cl,
			'pytest_para': result.pytest_para
		}
		return to_json
	except Exception as e:
		return {"desc": "暂未查询到数据,原因：%s" % str(e)}


def task_insert(post_json):
	task = TaskInfo(task_name=post_json['task_name'],
					associated_case=post_json['associated_case'],
					task_status=False,
					locust_cl=post_json['locust_cl'],
					pytest_para=post_json['pytest_para'])
	db.session.add(task)
	db.session.commit()


def task_update(put_json):
	result = TaskInfo.query.get(put_json['task_id'])
	result.task_name = put_json['task_name']
	result.associated_case = put_json['associated_case']
	result.task_status = put_json['task_status']
	result.locust_cl = put_json['locust_cl']
	result.pytest_para = put_json['pytest_para']
	db.session.commit()


def task_update_status(id, status):
	result = TaskInfo.query.get(id)
	result.task_status = status
	db.session.commit()


def task_cl_update(put_json):  # 2.0版本此接口弃用
	result = TaskInfo.query.get(put_json['task_id'])
	result.locust_cl = put_json['locust_cl']
	db.session.commit()


def task_delete(del_json):
	result = TaskInfo.query.get(del_json['task_id'])
	db.session.delete(result)
	db.session.commit()


def is_running():  # 判断locust是否在运行
	os = platform.architecture()[1]  # 获取平台操作系统
	if os == 'WindowsPE':
		check_cmd = 'tasklist -v | findstr locust'
		check_process = subprocess.Popen(check_cmd, shell=True, stdout=subprocess.PIPE)
		if check_process.stdout.readlines():
			return True
		else:
			return False
	else:
		check_cmd = 'ps -ef |grep locust |grep -v "grep" |wc -l'
		check_process = subprocess.Popen(check_cmd, shell=True, stdout=subprocess.PIPE)
		if check_process.stdout.readlines()[0] != b'0\n':  # 判断是否存在locust的进程
			return True
		else:
			return False


# report的相关操作
def report_insert(post_json):
	report = Report(report_name=post_json['report_name'],
					task_id=post_json['task_id'],
					create_date=post_json['create_date'],
					file_path=post_json['file_path'])
	db.session.add(report)
	db.session.commit()


def report_select():
	reports = Report.query.all()
	rl = []
	for i in range(len(reports)):
		to_json = {'rpt_id': reports[i].rpt_id,
				   'report_name': reports[i].report_name,
				   'task_id': reports[i].task_id,
				   'create_date': reports[i].create_date,
				   'file_path': reports[i].file_path}
		rl.append(to_json)
	return rl


def report_select_id(rpt_id):
	try:
		result = Report.query.get(rpt_id)
		to_json = {'rpt_id': result.rpt_id,
				   'report_name': result.report_name,
				   'task_id': result.task_id,
				   'create_date': result.create_date,
				   'file_path': result.file_path}
		return to_json
	except Exception as e:
		return {"desc": "暂未查询到数据,原因：%s" % str(e)}


def report_new_record(task_id, report_json):  # 根据任务id生成报告记录
	search_res = Report.query.filter(Report.task_id == task_id).first()
	if search_res is not None:  # 判断是否有记录
		search_res.report_name = report_json['report_name']
		search_res.task_id = report_json['task_id']
		search_res.create_date = report_json['create_date']
		search_res.file_path = report_json['file_path']
		db.session.commit()
	else:
		report_insert(report_json)


# report更新 暂未使用到
def report_update(data_json):
	result = Report.query.get(data_json['rpt_id'])
	result.report_name = data_json['report_name']
	result.task_id = data_json['task_id']
	result.create_date = data_json['create_date']
	result.file_path = data_json['file_path']
	db.session.commit()


"""API模板生成相关"""


# 删除上传的文件
def del_file(filename):
	PROJECT_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
	extensions = filename.rsplit('.', 1)[1]
	if extensions == 'json':
		file_path = os.path.join(PROJECT_PATH, 'api/static/json_file')
	elif extensions == 'xlsx':
		file_path = os.path.join(PROJECT_PATH, 'api/static/protobuf_xlsx')
	else:
		file_path = os.path.join(PROJECT_PATH, 'api/static/proto_file')
	os.remove(os.path.join(file_path, filename))


# 对上传的json文件解析后，入库到指定产品（api_json字段）
def json2templates(filename, product_id):
	"""
	:param filename: 文件名
	:param product_id: 产品ID
	:return: api_json写入product表的api_json字段
	"""
	file_path = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'api/static/json_file',
							 filename)
	with open(file_path, 'rb') as f:
		try:
			load_dict = json.load(f)['paths']  # 获取字典
		except Exception as e:
			print("模板文件内容格式有误，请确认后重试，原因：%s"%str(e))
		api_list = []
		for item in load_dict.items():  # api列表
			d = {}
			d[item[0]] = item[1]
			api_list.append(d)
	
	def get_values(dictionary):  # 获取元素值
		return list(list(dict.values(dictionary))[0].values())[0]
	
	result = []
	for i in api_list:  # 序列化想要的格式
		pre_dict = {}
		pre_dict['uri'] = list(i.keys())[0]
		pre_dict['function'] = get_values(i)['tags'][0]
		pre_dict['method'] = list(list(i.values())[0].keys())[0]
		if 'summary' in get_values(i):
			pre_dict['summary'] = get_values(i)['summary']
		else:
			pre_dict['summary'] = ''
		pre_dict['produces'] = {'content-type': 'application/json'}  # json格式的设置
		if len(get_values(i)['parameters']) > 0:
			pre_dict['parameters'] = get_values(i)['parameters'][0]
		else:
			pre_dict['parameters'] = get_values(i)['parameters']
		pre_dict['responses'] = get_values(i)['responses']
		result.append(pre_dict)
	put_json = {'pdt_id': product_id, 'api_json': result}
	pdt_update_api_json(put_json)


# 对上传的protobuf文件和接口文档解析，入库到指定产品（api_json字段）
def protobuf2templates(xlsx, product_id):
	"""
	:param xlsx: 读取excel的接口文档，获取url、method等信息
	:param proto: 从proto文件获取parameters
	:param product_id: 产品id
	:return:api_json写入product表的api_json字段
	"""
	project_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
	
	def read_excel():
		import xlrd
		xlsx_file = os.path.join(project_path, 'api/static/protobuf_xlsx', xlsx)
		with xlrd.open_workbook(xlsx_file) as wb:
			sheet_list = wb.sheet_names()  # 获取所有sheet名字
			api = []
			for name in sheet_list:
				sheet = wb.sheet_by_name(name)  # 通过名字获取sheet
				row_num = sheet.nrows  # 获取sheet行
				controller = sheet.row_values(1)[0]  # 处理合并单元格时，其他行可控制器值为空的情况
				for row in range(1, row_num):  # 遍历所有行
					api_dict = {}
					api_dict['function'] = name  # sheet名称定义为功能模块
					rows = sheet.row_values(row)  # 获取行内容
					api_dict['uri'] = '/api/%s/%s' % (controller, rows[1])
					api_dict['method'] = rows[2].lower()
					api_dict['summary'] = rows[-1]
					api_dict['produces'] = {'content-type': 'application/octet-stream'}
					api_dict['input_proto'] = rows[4]
					api_dict['message'] = rows[5]
					api.append(api_dict)  # 将每一行转换成dict，追加到apilist
			return api
	
	def get_params_from_proto(proto):
		import codecs
		with codecs.open(proto, 'r', encoding='utf-8', errors='ignore') as f:
			data = f.readlines()
			temp = [i for i in data if 'syntax' not in i and 'option' not in i]  # 去除无用信息
			two_lst = [s.split() for s in ''.join(temp).split('}') if s]  # 按'}'切割成多个子list
			two_lst = [x for x in two_lst if x != []]  # 去除空列表
			ls = []
			for li in two_lst:
				sub_list = []
				for i in li:
					if 'message' not in i:
						import re
						letter = ''.join(re.findall(r'[A-Za-z]', i))  # 获取字母串
						if letter != '':
							sub_list.append(letter)
				ls.append(sub_list)  # 获取到的params列表
				# 将结果转化成指定的字典
				try:
					list1 = [i[j] for i in ls for j in range(1)]
				except Exception as e:
					list1 = []
					print(str(e))
				list2 = []
				for sub in ls:
					dict1 = {}
					for i in range(1, len(sub) - 1, 2):
						dict1[sub[i + 1]] = sub[i]
					list2.append(dict1)
				json_dict = dict(zip(list1, list2))
				return json_dict
	
	# 将api_json入库
	doc = read_excel()
	api_list = []
	for api in doc:
		proto = api['input_proto']
		message = api['message']
		proto_file = os.path.join(project_path, 'api/static/proto_file', proto + '.proto')
		try:
			dic = get_params_from_proto(proto_file)
			for item in dic:
				if message == item:
					api['parameters'] = dic[message]
		except FileNotFoundError as e:
			print('file error:%s' % e)
		finally:
			api_list.append(api)
	put_json = {'pdt_id': product_id, 'api_json': api_list}
	pdt_update_api_json(put_json)


if __name__ == '__main__':
	# print(case_select_id(32)['api_weight'])
	# cases = CaseInfo.query.all()
	# print(json2templates('token.json'))
	# json2templates('token.json', 125)
	# protobuf2templates('eWordRIS25509214753577435745_transfer.xlsx', 105)
	# task_mlist()
	# json2templates('format_imcis1.json', 143)
	task_update_status(46,True)
