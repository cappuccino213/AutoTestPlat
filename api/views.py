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
import os
from flask_script import Manager
from werkzeug.utils import secure_filename

manager = Manager(app)


# 接口response消息格式化
def format_result(title, message, status):
	return {"title": title, "message": message, "status": status}


"""产品管理相关接口"""


# 产品列表
@app.route('/api/product/getproductlist', methods=['GET'])
def product_get():
	if request.method == 'GET':
		return jsonify(format_result('获取产品列表', pdt_select(), 200))
	else:
		return jsonify(format_result('405 Method Not Allowed', "The method is not allowed for the requested URL.", 405))


# 根据id查询产品
@app.route('/api/product/getproduct', methods=['GET'])
def product_get_id():
	if request.method == 'GET':
		pid = request.args.get('pid')
		return jsonify(format_result('获取id=%s的产品' % pid, pdt_select_id(pid), 200))


# 增加
@app.route('/api/product/addproducts', methods=['POST'])
def product_post():
	if request.method == 'POST':
		post_json = request.json
		try:
			pdt_insert(post_json)
			return jsonify(format_result('添加产品', 'successful', 200))
		except Exception as e:
			return jsonify(format_result('添加产品', 'failed,%s' % str(e), 400))


# 更新
@app.route('/api/product/updateproduct', methods=['PUT'])
def product_put():
	if request.method == 'PUT':
		put_json = request.json  # 用request内置的json方法序列化
		try:
			pdt_update(put_json)
			return jsonify(format_result('修改产品', 'successful', 201))
		except Exception as e:
			return jsonify(format_result('修改产品', 'failed,%s' % str(e), 400))


# 删除
@app.route('/api/product/delproduct', methods=['DELETE'])
def product_del():
	if request.method == 'DELETE':
		del_json = request.json
		try:
			pdt_delete(del_json)
			return jsonify(format_result('删除产品', 'successful', 204))
		except Exception as e:
			return jsonify(format_result('删除产品', 'failed,%s' % str(e), 400))


"""API管理相关接口"""


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
		post_json = request.json
		try:
			api_insert(post_json)
			return jsonify(format_result('添加API', 'successful', 200))
		except Exception as e:
			return jsonify(format_result('添加API', 'failed,%s' % str(e), 400))
	elif request.method == 'PUT':
		put_json = request.json
		try:
			api_update(put_json)
			return jsonify(format_result('修改API', 'successful', 201))
		except Exception as e:
			return jsonify(format_result('修改API', str(e), 400))
	elif request.method == 'DELETE':
		del_json = request.json
		try:
			api_delete(del_json)
			return jsonify(format_result('删除API', 'successful', 204))
		except Exception as e:
			return jsonify(format_result('删除API', 'failed,%s' % str(e), 400))
	else:
		return jsonify(format_result('405 Method Not Allowed', "The method is not allowed for the requested URL.", 405))


"""case管理相关接口"""


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
		post_json = request.json
		try:
			case_insert(post_json)
			return jsonify(format_result('添加CASE', 'successful', 200))
		except Exception as e:
			return jsonify(format_result('添加CASE', 'failed,%s' % str(e), 400))
	elif request.method == 'PUT':
		put_json = request.json
		try:
			case_update(put_json["type_id"], put_json)
			return jsonify(format_result('修改CASE', 'successful', 201))
		except Exception as e:
			return jsonify(format_result('修改CASE', str(e), 400))
	elif request.method == 'DELETE':
		del_json = request.json
		try:
			case_delete(del_json)
			return jsonify(format_result('删除CASE', 'successful', 204))
		except Exception as e:
			return jsonify(format_result('删除CASE', 'failed,%s' % str(e), 400))
	else:
		return jsonify(format_result('405 Method Not Allowed', "The method is not allowed for the requested URL.", 405))


"""任务管理相关接口"""


# task列表
@app.route('/api/taskinfo/tasklist', methods=['GET'])
def task_list():
	if request.method == 'GET':
		return jsonify(format_result('获取task列表', task_select(), 200))


# 任务管理列表内容
@app.route('/api/taskinfo/taskmagager', methods=['GET'])
def task_manager():
	if request.method == 'GET':
		return jsonify(format_result('获取task列表', task_mlist(), 200))


# task增删改查
@app.route('/api/taskinfo/task', methods=['GET', 'POST', 'PUT', 'DELETE'])
def task_handle():
	if request.method == 'GET':
		tid = request.args.get('tid')
		return jsonify(format_result('获取id=%s的task' % tid, task_select_id(tid), 200))
	elif request.method == 'POST':
		post_json = request.json
		try:
			task_insert(post_json)
			return jsonify(format_result('添加TASK', 'successful', 200))
		except Exception as e:
			return jsonify(format_result('添加TASK', 'failed,%s' % str(e), 400))
	elif request.method == 'PUT':
		put_json = request.json
		try:
			task_update(put_json)
			return jsonify(format_result('修改TASK', 'successful', 201))
		except Exception as e:
			return jsonify(format_result('修改TASK', str(e), 400))
	elif request.method == 'DELETE':
		del_json = request.json
		try:
			task_delete(del_json)
			return jsonify(format_result('删除TASK', 'successful', 204))
		except Exception as e:
			return jsonify(format_result('删除TASK', 'failed,%s' % str(e), 400))
	else:
		return jsonify(format_result('405 Method Not Allowed', "The method is not allowed for the requested URL.", 405))


# locust参数修改
@app.route('/api/taskinfo/task/locust', methods=['PUT'])  # 2.0版本此接口弃用
def task_locust():
	if request.method == 'PUT':
		put_json = request.json
		try:
			task_cl_update(put_json)
			return jsonify(format_result('修改locust参数', 'successful', 201))
		except Exception as e:
			return jsonify(format_result('修改locust参数', str(e), 400))


"""报告相关接口"""


# report列表
@app.route('/api/reportinfo/reportlist', methods=['GET'])
def report_list():
	if request.method == 'GET':
		return jsonify(format_result('获取report列表', report_select(), 200))


# 根据报告id查询报告
@app.route('/api/reportinfo/report', methods=['GET', 'POST'])
def report_handle():
	if request.method == 'GET':
		rid = request.args.get('rid')
		return jsonify(format_result('获取id=%s的report' % rid, report_select_id(rid), 200))
	elif request.method == 'POST':
		post_json = request.json
		try:
			report_insert(post_json)
			return jsonify(format_result('添加report', 'successful', 200))
		except Exception as e:
			return jsonify(format_result('添加report', 'failed,%s' % str(e), 400))
	else:
		return jsonify(format_result('405 Method Not Allowed', "The method is not allowed for the requested URL.", 405))


# 下载报告
@app.route('/api/report/download/<filename>', methods=['GET'])
def report_download(filename):
	"""
	:param diretory:本地目录的path
	:param filename: 文件名（带扩展名）
	"""
	if request.method == 'GET':
		project_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
		directory = os.path.join(project_path, 'report')  # 本地目录
		response = make_response(send_from_directory(directory, filename, as_attachment=True))
		response.headers["Content-Disposition"] = "attachment; filename={}".format(
			filename.encode().decode('latin-1'))  # 解决文件名中文问题
		return response


# 访问报告
@app.route('/api/report/access/<report_html>', methods=['GET'])
def report_access(report_html):
	return render_template(report_html)


"""页面访问相关"""


# 页面html文件路由绑定
# @app.route('/<file>', methods=['GET'])
# def index1(file):
# 	if '.' in file:
# 		if '.html' in file:
# 			return render_template(file)
# 		else:
# 			return 'failed,check your url if ends with "" or ".html'
# 	else:
# 		return render_template(file + '.html')


# 测试页面
# @app.route('/', methods=['GET'])
# def demo():
# 	return "test successfully"


# index.html进入前端应用
@app.route('/')
def index():
	return render_template('index.html')


"""性能测试流程相关接口"""


# 生成脚本
@app.route('/api/taskscript-performance', methods=['GET'])
def gnr_script():
	task_id = int(request.args.get('task_id'))
	try:
		from script.generate_script import GenerateScript
		gs = GenerateScript(task_id)
		gs.main()
		return jsonify(format_result('生成执行脚本', 'generate script successfully', 200))
	except Exception as e:
		return jsonify(format_result('生成执行脚本', 'generate script failed,%s' % str(e), 500))


# 启停性能测试任务
@app.route('/api/task-performance', methods=['GET'])
def locust_cl():
	"""
	停止任务，实例：
	http://192.168.1.21:8181/api/task-performance?order=0&task_id=10
	"""
	order = request.args.get('order')
	task_id = int(request.args.get('task_id'))
	from script.run_script import start, stop
	if request.method == 'GET':
		if order == '1':
			try:
				if not is_running():  # 同时只能运行一个locust任务
					task_update_status(task_id, True)
					start(task_id)  # 根据任务id加载对应的参数
					return jsonify(format_result('启动任务', 'start task successfully', 200))
				else:
					return jsonify(
						format_result('启动任务', 'failed:locust is already running by other task at the same time!', 500))
			except Exception as e:
				task_update_status(task_id, False)
				return jsonify(format_result('启动任务', 'start task failed,%s' % str(e), 500))
		elif order == '0':
			try:
				stop()
				task_update_status(task_id, False)
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


"""接口测试流程相关接口"""


# 生成测试脚本
@app.route('/api/taskscript-interface', methods=['GET'])
def gnr_in_script():
	task_id = int(request.args.get('task_id'))
	try:
		from script.generate_pytest_script import PytestScript
		gs = PytestScript(task_id)
		gs.main()
		return jsonify(format_result('生成执行脚本', 'generate script successfully', 200))
	except Exception as e:
		return jsonify(format_result('生成执行脚本', 'generate script failed,%s' % str(e), 500))


# 启动接口测试
@app.route('/api/task-interface', methods=['GET'])
def interface():
	if request.method == 'GET':
		task_id = int(request.args.get('task_id'))
		from script.run_pytest import main
		import os
		os.chdir(os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),
							  'script'))  # 修改当前工作目录为与script目录同级，不然收集不到测试的.py
		try:
			main(task_id)
			return jsonify(format_result('执行接口测试任务', 'task:%d finished' % task_id, 200))
		except Exception as e:
			return jsonify(format_result('执行接口测试任务', 'task:%d failed,reason:%s' % (task_id, str(e)), 500))


"""其他功能"""


# 用于判断文件后缀
def allowed_file(filename):
	ALLOWED_EXTENSIONS = {'xlsx', 'json', 'proto'}
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 上传文件
"""根据上传文件后缀名，上传到指定的类型目录"""


@app.route('/api/upload', methods=['POST', 'GET'], strict_slashes=Flask)
def upload_json():
	if request.method == 'POST':
		PROJECT_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
		file = request.files['file']
		if file and allowed_file(file.filename):  # 判断是否允许上传的类型
			filename = secure_filename(file.filename)
			extensions = filename.rsplit('.', 1)[1]
			if extensions == 'json':
				app.config['UPLOAD_FOLDER'] = os.path.join(PROJECT_PATH, 'api/static_old/json_file')
			elif extensions == 'xlsx':
				app.config['UPLOAD_FOLDER'] = os.path.join(PROJECT_PATH, 'api/static_old/protobuf_xlsx')
			else:
				app.config['UPLOAD_FOLDER'] = os.path.join(PROJECT_PATH, 'api/static_old/proto_file')
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return jsonify(format_result('上传文件', 'upload %s successfully' % filename, 200))
		else:
			return jsonify(format_result('上传文件',
										 'upload file failed,reason:please ensure your type of file is *.json、*.proto or *.xlsx',
										 500))


# 删除上传文件
@app.route('/api/upload-delete', methods=['GET'])
def upload_file_del():
	if request.method == 'GET':
		filename = request.args.get('filename')
		from api.controller import del_file
		try:
			del_file(filename)
			return jsonify(format_result('删除上传文件', 'delete %s successfully' % filename, 200))
		except Exception as e:
			return jsonify(format_result('删除上传文件', 'delete %s failed:%s' % (filename, str(e)), 500))


# 产品api模板-json
@app.route('/api/product/api-templates/json', methods=['POST'])
def json2api_templates():
	if request.method == 'POST':
		res_data = request.json
		try:
			json2templates(res_data['filename'], res_data['product_id'])
			return jsonify(format_result('生成api模板', 'generate templates successfully', 200))
		except Exception as e:
			return jsonify(format_result('生成api模板', 'generate templates failed:%s' % str(e), 500))


# 产品api模板-protobuf
@app.route('/api/product/api-templates/protobuf', methods=['POST'])
def protobuf2api_templates():
	if request.method == 'POST':
		res_data = request.json
		try:
			protobuf2templates(res_data['filename'], res_data['product_id'])
			return jsonify(format_result('生成api模板', 'generate templates successfully', 200))
		except Exception as e:
			return jsonify(format_result('生成api模板', 'generate templates failed:%s' % str(e), 500))


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=CONF['api_port'], threaded=True)
