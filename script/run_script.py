#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 10:18
# @Author  : Zhangyp
# @File    : run_script.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import os,subprocess,platform
from script.run_parameters import ScriptPara

def start(task_id):
	script_para = ScriptPara(task_id) # 脚本参数
	script_name = 'case_' + script_para.case_id[0] + '.py'  # 脚本名称
	if script_para.data_type()== 'json':
		type_path ='json_script'
	else:
		type_path = 'proto_script'
	script_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), type_path,
							   script_name)  # 脚本文件
	locust_option = script_para.locust_option()  # 运行参数
	ls_command = ["locust", "-f"]
	ls_command.append(script_file)
	ls_command += locust_option.split()  # 因为这边得到字符串,如"--host=127.0.0.1 --web-host=192.168.1.56 --web-port=8188",为subprocess的列表取值方式用split进行切割
	lo_process = subprocess.Popen(ls_command, stdout=subprocess.PIPE)
	print(lo_process.stdout.readlines())


def stop():
	os = platform.architecture()[1]
	if os == 'WindowsPE':  # 判断运行环境是否windows
		kill_cmd = 'taskkill /F /IM locust.exe'
	else:
		kill_cmd = 'killall -9 locust'  # 默认为linux
	kill_process = subprocess.Popen(kill_cmd, shell=True, stdout=subprocess.PIPE)
	out_message = kill_process.stdout.readlines()
	print(out_message)

def is_running():
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
		
if __name__=='__main__':
	start(10)