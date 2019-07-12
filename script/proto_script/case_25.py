import sys
sys.path.append("D:\flask-project\ApiPerformanceTest")
from locust import TaskSet, task, HttpLocust

class case_25Task(TaskSet):

	def on_start(self):
		print("start programing...")

	@task(1)
	def getdictypelist(self):
		from script.proto_script.DicTypeMstInputProto_pb2 import DicTypeMstInputProto
		url = "http://192.168.1.18:8150/api/dic/getdictypelist"
		header = {'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiMzI0ZjliZDgtY2RiZC00MjgyLWE4YTctZWFhMzE1YmM2NjFkIiwiaWF0IjoiMjAxOS83LzUgMTg6MTU6MzEiLCJleHAiOjE1NjIzNzkzMzEsImlzcyI6ImVXb3JkIiwiYXVkIjoiZVdvcmRQT0QifQ.f6lTZz4rh0YzOTdYv2dli4TmhrK_dUuDpZB91HAgwow'}
		body = DicTypeMstInputProto()
		body.pageSize = int
		body.typeCode = string
		body.typeName = string
		body.typeClass = string
		body.currentPage = int
		data = body.SerializeToString()
		name = "获取字典分类"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

class case_25User(HttpLocust):
	task_set = case_25Task
	min_wait = 1000
	max_wait = 2000
