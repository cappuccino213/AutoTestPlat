import sys
sys.path.append("D:\flask-project\AutoTestPlat")
sys.path.append("D:\flask-project\AutoTestPlat\script\json_script")
from locust import TaskSet, task, HttpLocust

class case_49Task(TaskSet):

	def on_start(self):
		print('start programing...')

	@task(1)
	def gettoken(self):
		url = '192.168.1.18:1122/api/authorize/gettoken'
		header = {'content-type': 'application/json'}
		body = {'in': 'query', 'name': 'input', 'type': 'string', 'required': False, 'description': ''}
		name = '获取token'
		response = self.client.post(url, json=body, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

class case_49user(HttpLocust):
	task_set = case_49Task
	min_wait = 1000
	max_wait = 2000
