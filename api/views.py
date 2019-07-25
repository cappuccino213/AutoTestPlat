#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 17:14
# @Author  : Zhangyp
# @File    : views.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask import request, jsonify, render_template, send_from_directory, make_response
from api.controller import *
from appconfig.read_ini import CONF
import json
import os
from flask_script import Manager

manager = Manager(app)
# 格式化返回结果
def format_result(title, message, status):
	return {"title": title, "message": message, "status": status}


# 产品路由
@app.route('/api/product/getproductlist', methods=['GET'])
def product_get():
	if request.method == 'GET':
		return jsonify(format_result('获取产品列表', pdt_select(), 200))
	else:
		return jsonify(format_result('405 Method Not Allowed', "The method is not allowed for the requested URL.", 405))


@app.route('/api/product/getproduct', methods=['GET'])
def product_get_id():
	if request.method == 'GET':
		pid = request.args.get('pid')
		return jsonify(format_result('获取id=%s的产品' % pid, pdt_select_id(pid), 200))


@app.route('/api/product/addproducts', methods=['POST'])
def product_post():
	if request.method == 'POST':
		post_json = json.loads(request.data)
		try:
			pdt_insert(post_json)
			return jsonify(format_result('添加产品', 'successful', 200))
		except Exception as e:
			return jsonify(format_result('添加产品', 'failed,%s' % str(e), 400))


@app.route('/api/product/updateproduct', methods=['PUT'])
def product_put():
	if request.method == 'PUT':
		put_json = json.loads(request.data)
		try:
			pdt_update(put_json)
			return jsonify(format_result('修改产品', 'successful', 201))
		except Exception as e:
			return jsonify(format_result('修改产品', 'failed,%s' % str(e), 400))


@app.route('/api/product/delproduct', methods=['DELETE'])
def product_del():
	if request.method == 'DELETE':
		del_json = json.loads(request.data)
		try:
			pdt_delete(del_json)
			return jsonify(format_result('删除产品', 'successful', 204))
		except Exception as e:
			return jsonify(format_result('删除产品', 'failed,%s' % str(e), 400))


# API路由
@app.route('/api/apiinfo/apilist', methods=['GET'])
def api_list():
	if request.method == 'GET':
		return jsonify(format_result('获取api列表', api_select(), 200))


# API的增删改查
@app.route('/api/apiinfo/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_handle():
	if request.method == 'GET':
		if ('aid' in request.args) and (request.args['aid']):
			aid = request.args['aid']
			return jsonify(format_result('获取aid=%s的api' % aid, api_select_id(aid), 200))
		if ('pid' in request.args) and (request.args['pid']):
			pid = request.args['pid']
			return jsonify(format_result('获取pid=%s的api' % pid, api_select_filter(pid), 200))
	elif request.method == 'POST':
		post_json = json.loads(request.data)
		try:
			api_insert(post_json)
			return jsonify(format_result('添加API', 'successful', 200))
		except Exception as e:
			return jsonify(format_result('添加API', 'failed,%s' % str(e), 400))
	elif request.method == 'PUT':
		put_json = json.loads(request.data)
		try:
			api_update(put_json)
			return jsonify(format_result('修改API', 'successful', 201))
		except Exception as e:
			return jsonify(format_result('修改API', str(e), 400))
	elif request.method == 'DELETE':
		del_json = json.loads(request.data)
		try:
			api_delete(del_json)
			return jsonify(format_result('删除API', 'successful', 204))
		except Exception as e:
			return jsonify(format_result('删除API', 'failed,%s' % str(e), 400))
	else:
		return jsonify(format_result('405 Method Not Allowed', "The method is not allowed for the requested URL.", 405))


# case路由
@app.route('/api/caseinfo/caselist', methods=['GET'])
def case_list():
	if request.method == 'GET':
		return jsonify(format_result('获取case列表', case_select(), 200))


@app.route('/api/caseinfo/case', methods=['GET', 'POST', 'PUT', 'DELETE'])
def case_handle():
	if request.method == 'GET':
		cid = request.args.get('cid')
		return jsonify(format_result('获取id=%s的case' % cid, case_select_id(cid), 200))
	elif request.method == 'POST':
		post_json = json.loads(request.data)
		try:
			case_insert(post_json)
			return jsonify(format_result('添加CASE', 'successful', 200))
		except Exception as e:
			return jsonify(format_result('添加CASE', 'failed,%s' % str(e), 400))
	elif request.method == 'PUT':
		put_json = json.loads(request.data)
		try:
			case_update(put_json)
			return jsonify(format_result('修改CASE', 'successful', 201))
		except Exception as e:
			return jsonify(format_result('修改CASE', str(e), 400))
	elif request.method == 'DELETE':
		del_json = json.loads(request.data)
		try:
			case_delete(del_json)
			return jsonify(format_result('删除CASE', 'successful', 204))
		except Exception as e:
			return jsonify(format_result('删除CASE', 'failed,%s' % str(e), 400))
	else:
		return jsonify(format_result('405 Method Not Allowed', "The method is not allowed for the requested URL.", 405))


# task路由绑定
@app.route('/api/taskinfo/tasklist', methods=['GET'])
def task_list():
	if request.method == 'GET':
		return jsonify(format_result('获取task列表', task_select(), 200))


@app.route('/api/taskinfo/task', methods=['GET', 'POST', 'PUT', 'DELETE'])
def task_handle():
	if request.method == 'GET':
		tid = request.args.get('tid')
		return jsonify(format_result('获取id=%s的task' % tid, task_select_id(tid), 200))
	elif request.method == 'POST':
		post_json = json.loads(request.data)
		try:
			task_insert(post_json)
			return jsonify(format_result('添加TASK', 'successful', 200))
		except Exception as e:
			return jsonify(format_result('添加TASK', 'failed,%s' % str(e), 400))
	elif request.method == 'PUT':
		put_json = json.loads(request.data)
		try:
			task_update(put_json)
			return jsonify(format_result('修改TASK', 'successful', 201))
		except Exception as e:
			return jsonify(format_result('修改TASK', str(e), 400))
	elif request.method == 'DELETE':
		del_json = json.loads(request.data)
		try:
			task_delete(del_json)
			return jsonify(format_result('删除TASK', 'successful', 204))
		except Exception as e:
			return jsonify(format_result('删除TASK', 'failed,%s' % str(e), 400))
	else:
		return jsonify(format_result('405 Method Not Allowed', "The method is not allowed for the requested URL.", 405))


@app.route('/api/taskinfo/task/locust', methods=['PUT']) # 2.0版本此接口弃用
def task_locust():
	if request.method == 'PUT':
		put_json = json.loads(request.data)
		try:
			task_cl_update(put_json)
			return jsonify(format_result('修改locust参数', 'successful', 201))
		except Exception as e:
			return jsonify(format_result('修改locust参数', str(e), 400))


# report路由绑定
@app.route('/api/reportinfo/reportlist', methods=['GET'])
def report_list():
	if request.method == 'GET':
		return jsonify(format_result('获取report列表', report_select(), 200))


@app.route('/api/reportinfo/report', methods=['GET', 'POST'])
def report_handle():
	if request.method == 'GET':
		rid = request.args.get('rid')
		return jsonify(format_result('获取id=%s的report' % rid, report_select_id(rid), 200))
	elif request.method == 'POST':
		post_json = json.loads(request.data)
		try:
			report_insert(post_json)
			return jsonify(format_result('添加report', 'successful', 200))
		except Exception as e:
			return jsonify(format_result('添加report', 'failed,%s' % str(e), 400))
	else:
		return jsonify(format_result('405 Method Not Allowed', "The method is not allowed for the requested URL.", 405))


# 下载报告文件
@app.route('/viewreport/<filename>', methods=['GET'])
def download_file(filename):
	cur_path = os.path.abspath(os.path.dirname(__file__))  # 当前目录
	directory = os.path.join(cur_path, 'report')
	print(directory)
	response = make_response(send_from_directory(directory, filename, as_attachment=True))
	response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
	return response


# html文件路由绑定
@app.route('/<file>', methods=['GET'])
def index(file):
	if '.' in file:
		if '.html' in file:
			return render_template(file)
		else:
			return 'failed,check your url if ends with "" or ".html'
	else:
		return render_template(file + '.html')


# 测试页面
@app.route('/', methods=['GET'])
def demo():
	return "test successfully"


# 生成脚本
@app.route('/api/taskscript', methods=['GET'])
def gnr_script():
	task_id = int(request.args.get('task_id'))
	try:
		from script.generate_script import GenerateScript
		gs = GenerateScript(task_id)
		gs.main()
		return jsonify(format_result('生成执行脚本', 'generate script successfully', 200))
	except Exception as e:
		return jsonify(format_result('生成执行脚本', 'generate script failed,%s' % str(e), 500))


# 启停任务
@app.route('/api/task-performance', methods=['GET'])
def locust_cl():
	"""
	停止任务，实例：
	http://192.168.1.21:8181/api/task-performance?order=0&task_id=10
	"""
	order = request.args.get('order')
	task_id = int(request.args.get('task_id'))
	from script.run_script import start,stop
	if request.method == 'GET':
		if order == '1':
			try:
				start(task_id)  # 根据任务id加载对应的参数
				return jsonify(format_result('启动任务', 'start task successfully', 200))
			except Exception as e:
				return jsonify(format_result('启动任务', 'start task failed,%s' % str(e), 500))
		elif order == '0':
			try:
				stop()
				return jsonify(format_result('停止任务', 'stop task successfully', 200))
			except Exception as e:
				return jsonify(format_result('停止任务', 'stop task failed,%s' % str(e), 500))
		else:
			return jsonify(
				format_result('url error', '/api/task-performance?order=<int>&task_id=<int>', 400))


# 检查locust是否运行成功
@app.route('/api/task/check-locust', methods=['GET'])
def check_locust():
	if request.method == 'GET':
		from script.run_script import is_running
		status = is_running()
		return jsonify(format_result('locust运行状态', status, 200))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=CONF['api_port'],threaded=True)