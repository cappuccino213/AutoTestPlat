#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 14:04
# @Author  : Zhangyp
# @File    : controller.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from api.modles import *


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
	# result = Product.query.filter_by(pdt_id=data['pdt_id']).first()
	result = Product.query.get(put_json['pdt_id'])  # 通过主键查询
	result.pdt_name = put_json['pdt_name']
	result.version = put_json['version']
	result.host = put_json['host']
	result.description = put_json['description']
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
				   'api_expection': cases[i].api_expection}
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
			'api_expection': result.api_expection
		}
		return to_json
	except Exception as e:
		return {"desc": "暂未查询到数据,原因：%s" % str(e)}


def case_insert(post_json):
	case = CaseInfo(case_name=post_json['case_name'],
					api_weight=post_json['api_weight'],
					type_id=post_json['type_id'],
					api_expection=post_json['api_expection'])
	db.session.add(case)
	db.session.commit()


def case_update(put_json):
	result = CaseInfo.query.get(put_json['case_id'])
	result.case_name = put_json['case_name']
	result.api_weight = put_json['api_weight']
	result.type_id = put_json['type_id']
	result.api_expection = put_json['api_expection']
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


def task_cl_update(put_json):  # 2.0版本此接口弃用
	result = TaskInfo.query.get(put_json['task_id'])
	result.locust_cl = put_json['locust_cl']
	db.session.commit()


def task_delete(del_json):
	result = TaskInfo.query.get(del_json['task_id'])
	db.session.delete(result)
	db.session.commit()


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

if __name__ == '__main__':
	print(case_select_id(32)['api_weight'])
	# cases = CaseInfo.query.all()
# 	# for i in cases:
# 	# 	print(type(i),i)
# 	task_id = report_new_record['task_id']
# 	print(type(task_id),task_id)
