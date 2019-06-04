from script.script_class import ScriptPara
def generate_script(task_id):
	"""
	1.获取类名--case_name
	2.获取函数名--api_url最后一个"/"内容
	3.获取http请求方法类型，对应生成不同的函数
	4.获取函数参数url(host+url)、headers(是否需要授权token)、body、title(api_name(api_url))
	5.生成脚本文件--脚本名为case_id名
	"""
	
	#  定义各代码块需要的参数
	sp = ScriptPara(task_id) #这里的任务id来自前端，点击生成脚本后，把对应的任务id传进来
	CLASSNAME = 'case_'+sp.case_id[0] #script 类名
	FUNCTION = [i['url'].split('/')[-1].lower() for i in sp.para]# script 函数名
	WEIGHT = [int(i['weight']) for i in sp.weight]
	METHOD = [i['method'].upper() for i in sp.para] # script 方法
	URL = [i+j['url']for i,j in zip(sp.host,sp.para)] # 同时遍历两个list拼接url
	TOKEN = sp.token # 获取token
	
	for i in sp.para: # 根据是否需要token，将token加入headers
		if i['has_token']:
			i['header']['Authorization']=TOKEN
	HEADERS = [i['header']for i in sp.para]
	BODY = [i['body'] for i in sp.para]
	VALUES = [i['values'] for i in sp.para]
	TITLE = [i['url']+'('+j['api_name']+')' for i,j in zip(sp.para,sp.para)] # api测试名称
	MIN = sp.min_wait
	MAX = sp.max_wait
	# print(FUNCTION)
	# print(WEIGHT)
	# print(METHOD)
	# print(URL)
	# print(HEADERS)
	print(VALUES)
	# print(TITLE)
	# print(MIN)
	# print(MAX)
	
	"""
	脚本拼接
	将各个代码块装进list，然后一行行写入
	"""
	package_code = ["from locust import TaskSet, task, HttpLocust"]
	TaskSet_code = ["class %sTask(TaskSet):"%CLASSNAME,
					"def on_start(self):",
					"print('start programing...')"]
	function_code = []
	for i in range(len(FUNCTION)):
		function_code.append("@task(%d)"%WEIGHT[i])
		function_code.append("def %s(self):"%FUNCTION[i])
		if METHOD[i]=='POST':
			function_code.append("url = '%s'"%URL[i])
			function_code.append("header = %s"%HEADERS[i])
			function_code.append("body = %s"%BODY[i])
			function_code.append("name = '%s'"%TITLE[i])
			function_code.append("response = self.client.post(url, json=body, headers=header, name=name)")
			function_code.append("print(response.status_code, response.text)")
			function_code.append("response.raise_for_status()")
		if METHOD[i] == 'GET':
			function_code.append("url = '%s%s'" % (URL[i],VALUES[i]))
			function_code.append("header = %s" % HEADERS[i])
			function_code.append("name = '%s'" % TITLE[i])
			function_code.append("response = self.client.get(url, headers=header, name=name)")
			function_code.append("print(response.status_code, response.text)")
			function_code.append("response.raise_for_status()")
		
	HttpLocust_code = ["class %sUser(HttpLocust):"%CLASSNAME,
					  "task_set = %sTask"%CLASSNAME,
					  "min_wait = %d"%MIN,
					  "max_wait = %d"%MAX]

	"""
	将个list顺序写入py文件
	"""
	import os
	current_path = os.path.abspath(os.path.dirname(__file__))
	with open('%s/%s.py' % (current_path,CLASSNAME), 'w+', encoding='UTF-8') as w:
		for i in package_code:
			w.write(str(i) + '\n')
		for i in TaskSet_code:
			if i.startswith('class'):
				w.write(str(i) + '\n')
			elif i.startswith('def'):
				w.write('\n' + '\t' + str(i) + '\n')
			else:
				w.write('\t\t' + str(i) + '\n')
		for i in function_code:
			if i.startswith('class'):
				w.write(str(i) + '\n')
			elif i.startswith('@'):
				w.write('\n' + '\t' + str(i))
			elif i.startswith('def'):
				w.write('\n' + '\t' + str(i) + '\n')
			else:
				w.write('\t\t' + str(i) + '\n')
		for i in HttpLocust_code:
			if i.startswith('class'):
				w.write('\n' + str(i) + '\n')
			else:
				w.write('\t' + str(i) + '\n')
				
if __name__=='__main__':
	generate_script(10)