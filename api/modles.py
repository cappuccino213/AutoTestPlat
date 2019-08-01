#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 15:09
# @Author  : Zhangyp
# @File    : modles.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from logging.config import dictConfig

# 日志配置
dictConfig({
	'version': 1,
	'formatters': {'default': {
		'format': '''[时间]:%(asctime)s
[线程]:%(thread)s
[级别]:%(levelname)s
[信息]:%(message)s
------------------
	''',
	}},
	'handlers': {'wsgi': {
		'class': 'logging.StreamHandler',
		'stream': 'ext://flask.logging.wsgi_errors_stream',
		'formatter': 'default'
	}},
	'root': {
		'level': 'INFO',
		'handlers': ['wsgi']
	}
})

app = Flask(__name__, static_folder='static', static_url_path='/static')  # 定义静态文件的名字和目录
CORS(app, supports_credentials=True)  # 处理跨域问题
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


class Product(db.Model):
	__tablename__ = "product"  # 表名会自动生成(可不用定义)，根据类名派生出，转成小写，如“CamelCase” 转换为 “camel_case”
	pdt_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
	pdt_name = db.Column(db.String(32), unique=True)
	version = db.Column(db.String(32))
	description = db.Column(db.String(128))
	host = db.Column(db.String(64))
	api_info = db.relationship('ApiInfo', backref='product', lazy='dynamic')
	api_json = db.Column(db.JSON)
	delete_flag = db.Column(db.Boolean,default=False)


class ApiInfo(db.Model):
	api_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
	api_name = db.Column(db.String(128), unique=True)
	method = db.Column(db.String(16))
	url = db.Column(db.String(128))
	header = db.Column(db.JSON)
	body = db.Column(db.JSON)
	has_token = db.Column(db.Boolean,default=False)
	pdt_id = db.Column(db.Integer, db.ForeignKey('product.pdt_id'))
	values = db.Column(db.String(128))
	proto_file = db.Column(db.String(64))
	proto_message = db.Column(db.String(64))
	


class CaseInfo(db.Model):
	case_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
	case_name = db.Column(db.String(32), unique=True)
	api_weight = db.Column(db.JSON)
	type_id = db.Column(db.SmallInteger)
	api_expection = db.Column(db.JSON)


class RelationInfo(db.Model):
	rlt_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
	case_id = db.Column(db.Integer, db.ForeignKey('case_info.case_id'))
	api_id = db.Column(db.Integer, db.ForeignKey('api_info.api_id'))
	weight = db.Column(db.SmallInteger,default=1)


class TestType(db.Model):  # 测试类型，今后扩展自动化平台用
	type_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
	type_name = db.Column(db.String(32), unique=True)


# class RelationInfo(db.Model):
# 	rlt_id = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
# 	case_id = db.Column(db.Integer,db.ForeignKey('case_info.case_id'))
# 	api_id = db.Column(db.Integer,db.ForeignKey('api_info.api_id'))

class TaskInfo(db.Model):
	task_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
	task_name = db.Column(db.String(32), unique=True)
	associated_case = db.Column(db.JSON)
	task_status = db.Column(db.Boolean,default=False)
	locust_cl = db.Column(db.JSON)
	pytest_para = db.Column(db.JSON)

class Report(db.Model):
	rpt_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
	report_name = db.Column(db.String(32), unique=True)
	# case_id = db.Column(db.Integer, db.ForeignKey('case_info.case_id'))
	task_id = db.Column(db.Integer,db.ForeignKey('task_info.task_id'))
	create_date = db.Column(db.DateTime)
	file_path = db.Column(db.String(255))
