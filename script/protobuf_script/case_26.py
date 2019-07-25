import sys
sys.path.append("D:\flask-project\ApiPerformanceTest")
sys.path.append("D:\flask-project\ApiPerformanceTest\script\proto_script")
from locust import TaskSet, task, HttpLocust

class case_26Task(TaskSet):

	def on_start(self):
		print("start programing...")

	@task(2)
	def getcheckinfolist(self):
		from script.proto_script.CheckInfoProto_pb2 import SearchInputProto
		url = "http://192.168.1.18:8150/api/check/getcheckinfolist"
		header = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNGYyZGYzYzAtMjUxMS00ZDgwLTkyMzgtNTc4NTFkNDJmODEyIiwiaWF0IjoiMjAxOS83LzE3IDE4OjIwOjQxIiwiZXhwIjoxNTYzNDE2NDQxLCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.RVmgoefvFi0ocWyn2VsLllFeiXyZM5Lu8KWFagV8-j8'}
		body = SearchInputProto()
		body.examEndTime = "2019-05-01 23:59:59"
		body.examStartTime = "2018-11-01 00:00:00"
		body.organizationID = "local"
		data = body.SerializeToString()
		name = "获取检查信息列表（半年）"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

	@task(3)
	def getcheckinfolist_1(self):
		from script.proto_script.CheckInfoProto_pb2 import SearchInputProto
		url = "http://192.168.1.18:8150/api/check/getcheckinfolist"
		header = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNGYyZGYzYzAtMjUxMS00ZDgwLTkyMzgtNTc4NTFkNDJmODEyIiwiaWF0IjoiMjAxOS83LzE3IDE4OjIwOjQxIiwiZXhwIjoxNTYzNDE2NDQxLCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.RVmgoefvFi0ocWyn2VsLllFeiXyZM5Lu8KWFagV8-j8'}
		body = SearchInputProto()
		body.accessionNumber = "396304"
		data = body.SerializeToString()
		name = "获取检查信息列表（单个检查号）"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

	@task(4)
	def getvisitpeople(self):
		from script.proto_script.VisitInputProto_pb2 import VisitInputProto
		url = "http://192.168.1.18:8150/api/clinic/getvisitpeople"
		header = {'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNGYyZGYzYzAtMjUxMS00ZDgwLTkyMzgtNTc4NTFkNDJmODEyIiwiaWF0IjoiMjAxOS83LzE3IDE4OjIwOjQxIiwiZXhwIjoxNTYzNDE2NDQxLCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.RVmgoefvFi0ocWyn2VsLllFeiXyZM5Lu8KWFagV8-j8'}
		body = VisitInputProto()
		body.ageUnit = "岁"
		body.admitEndDate = "2019-01-31 23:59:59"
		body.admitStartDate = "2018-07-01 00:00:00"
		data = body.SerializeToString()
		name = "获取就诊视图列表（半年）"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

	@task(4)
	def getcheckinfolist_2(self):
		from script.proto_script.CheckInfoProto_pb2 import SearchInputProto
		url = "http://192.168.1.18:8150/api/check/getcheckinfolist"
		header = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiNGYyZGYzYzAtMjUxMS00ZDgwLTkyMzgtNTc4NTFkNDJmODEyIiwiaWF0IjoiMjAxOS83LzE3IDE4OjIwOjQxIiwiZXhwIjoxNTYzNDE2NDQxLCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.RVmgoefvFi0ocWyn2VsLllFeiXyZM5Lu8KWFagV8-j8'}
		body = SearchInputProto()
		body.examEndTime = "2018-12-01 23:59:59"
		body.examStartTime = "2018-11-01 00:00:00"
		body.organizationID = "local"
		data = body.SerializeToString()
		name = "获取检查信息列表（一个月）"
		response = self.client.post(url, data=data, headers=header, name=name)
		result = response.text
		print(response.status_code, result)
		response.raise_for_status()

class case_26User(HttpLocust):
	task_set = case_26Task
	min_wait = 1000
	max_wait = 2000
