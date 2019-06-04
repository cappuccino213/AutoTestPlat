#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 9:33
# @Author  : Zhangyp
# @File    : locust_run.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import os

# 自动打开浏览器 做到前端
def open_browser(url):
	from read_config.read_ini import CLIENTPATH
	import webbrowser
	try:
		print('try to open chrome...')
		webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(CLIENTPATH))
		webbrowser.get('chrome').open(url,new=1,autoraise=True)#new=1,打开新的窗口；autoraise=True，窗口前置
	except Exception as e:
		print('open chrome failed:%s,please open browser access'%str(e))

# 启动locust
def locust_start(task_id):
	from script.script_class import ScriptPara # 为了导入生成文件的名称 # 导入locust的选项命令
	sp = ScriptPara(task_id)
	script_name='case_'+sp.case_id[0] # 脚本名称
	option = sp.locust_option() # 运行命令
	current_path = os.path.abspath(os.path.dirname(__file__))
	cmd_line = 'locust -f %s/%s.py %s'%(current_path,script_name,option)# 1改成前端传的task_id
	# cmd_line = 'locust -f locust_script_gn.py %s'%locust_option(task_id)# 1改成前端传的task_id
	# open_browser(sp.locust_url)
	try:
		p = os.popen(cmd_line)
		print(p.read())
	except Exception as e:
		print(str(e))
	
# 停止locust
def locust_stop():
	cmd_line = 'taskkill /F /IM locust.exe'
	p = os.popen(cmd_line)
	print(p.read())
	
if __name__=="__main__":
	# open_browser('http://192.168.1.56:8182')
	locust_start(10)
	# locust_stop()
