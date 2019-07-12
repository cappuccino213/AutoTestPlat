from locust import TaskSet, task, HttpLocust

class case_23Task(TaskSet):

	def on_start(self):
		print('start programing...')

	@task(1)
	def login(self):
		url = 'http://192.168.1.58:8092/Home/Login'
		header = {'content-type': 'application/json'}
		body = {'account': 'jm', 'password': 'e10adc3949ba59abbe56e057f20f883e', 'loginType': '0'}
		name = '登录'
		response = self.client.post(url, json=body, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

	@task(1)
	def checkport(self):
		url = 'http://192.168.1.58:8092/Admin/Config/CheckPort?port=108'
		header = {'content-type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNDZkNjNlZmEtNGY5Yi00M2U2LThjYWUtMDQ2MWMyM2U2MTI2IiwiaWF0IjoiMjAxOS83LzUgMTQ6NTg6MjAiLCJleHAiOjE1NjIzNjc1MDAsImlzcyI6ImVXb3JkIiwiYXVkIjoiZVdvcmRQT0QifQ.BoqJRTYUrMg03W_zn53TJ5_SffUNejTmICPTlJP9HlI'}
		name = '测试端口是否占用'
		response = self.client.get(url, headers=header, name=name)
		print(response.status_code, response.text)
		response.raise_for_status()

class case_23user(HttpLocust):
	task_set = case_23Task
	min_wait = 1000
	max_wait = 2000
