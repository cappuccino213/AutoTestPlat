# -*- coding: utf-8 -*-
# generate time:2019-09-16 17:28:50


import requests

def verify(res,expection):
	if res.status_code == expection['status_code']:
		return True
	else:
		return False
		

def test_registeruser():
	headers = {'userinfo': "{'useruid': '29d6a026-f774-4c9d-904c-e492a4246e10', 'organizationid': '-1'}", 'content-type': 'application/octet-stream', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Inp5cCIsIkN1c3RvbURhdGEiOiJcIlwiIiwianRpIjoiYmZkMDQxMzgtNmM5Ni00Y2Q3LTlhNjgtYTRhZTA3MDc5N2U1IiwiaWF0IjoiMjAxOS85LzE2IDE3OjI4OjUyIiwiZXhwIjoxNTY4NjgzNzMyLCJpc3MiOiJlV29yZCIsImF1ZCI6ImVXb3JkUE9EIn0.HgOjN6D348fdAAWZZV2ODmlC09ZHS9ndHdxbtds_Ezg'}
	expection = {'messege': {}, 'status_code': 200}
	from script.protobuf_script.UserMstProto_pb2 import UserMstProto
	url = "http://192.168.1.8:8150/api/register/registeruser"
	data = UserMstProto()
	data.name = "测试"
	data.type = "doctor"
	data.email = "2545854526@qq.com"
	data.deptID = "02332bb9-1f92-4b26-bbe0-d37408b1d492"
	data.status = "0"
	data.workNO = "8512"
	data.account = "test"
	data.address = "杭州紫金花路"
	data.iDCardNO = "352458855452562558"
	data.password = "123456"
	data.createDate = "2019-7-11 13：55：48.297"
	data.officePhone = "0571-85652548"
	data.privatePhone = "15865254528"
	data.createUserUID = "00000000-0000-0000-0000-000000000000"
	data.createUserName = "用户自己注册"
	data.organizationID = "local"
	data = data.SerializeToString()
	res = requests.request(method="POST", url=url, data=data, headers=headers)
	assert verify(res, expection)
