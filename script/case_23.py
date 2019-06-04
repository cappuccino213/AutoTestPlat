from locust import TaskSet, task, HttpLocust
class case_23Task(TaskSet):

	def on_start(self):
		print('start programing...')

	@task(1)
	def login(self):
		url = 'http://192.168.1.58:8092/Home/Login'
		header = {'Content-Type': 'application/json'}
		body = {'account': 'jm', 'password': 'e10adc3949ba59abbe56e057f20f883e', 'loginType': '0'}
		name = '/Home/Login(登录)'
		response = self.client.post(url, json=body, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

	@task(1)
	def checkport(self):
		url = 'http://192.168.1.58:8092/Admin/Config/CheckPort?port=108'
		header = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiMjBjZjgzMDEtZTZlZC00MjFjLTk2NDctNzU4ZDRjMDYzNzJmIiwiaWF0IjoiMjAxOS81LzI5IDE4OjQ4OjUyIiwiZXhwIjoxNTU5MTg0NTMyLCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.oHckGcz7d_qF-sssrzjRu1eqG-UvZRR2uZi5cCpguGA'}
		name = '/Admin/Config/CheckPort(测试端口是否占用)'
		response = self.client.get(url, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

	@task(1)
	def getmatfailedcount(self):
		url = 'http://192.168.1.58:8092/Film/GetMatFailedCount'
		header = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiMjBjZjgzMDEtZTZlZC00MjFjLTk2NDctNzU4ZDRjMDYzNzJmIiwiaWF0IjoiMjAxOS81LzI5IDE4OjQ4OjUyIiwiZXhwIjoxNTU5MTg0NTMyLCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.oHckGcz7d_qF-sssrzjRu1eqG-UvZRR2uZi5cCpguGA'}
		name = '/Film/GetMatFailedCount(获取匹配失败数量1)'
		response = self.client.get(url, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

class case_23User(HttpLocust):
	task_set = case_23Task
	min_wait = 1000
	max_wait = 2000
