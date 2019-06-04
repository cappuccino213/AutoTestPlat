//-------展示api列表
var flag = 0;
$.ajax({
	url: '' + host + '/api/apiinfo/apilist',
	type: 'get',
	dataType: 'json',
	success: function(data) {
		$.each(data.message, function(index, item) {
			console.log("数据对象1：" + item.pdt_id);
			var id = item.pdt_id;
			//console.log("数据对象：" + id);
			var div = "";
			div = '<td>' + item.api_name + '</td>' +
				'<td>' + item.method + '</td>' +
				'<td id="pdt' + item.api_id + '' + item.pdt_id + '"></td>' +
				'<td><table width="100" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td><a href="#" id="dela1" onclick="del(this)" type="' +
				item.api_id + '" ><img src="../static/img/u48.svg"></td><td><a href="updateAPI.html?id=' + item.api_id +
				'"><img src="../static/img/u50.svg"></a></td></tr></table></td></tr>';
			$("#tbody-result").append('<tr id="' + item.pdt_id + '">' + div + '</tr>')

			$.ajax({
				url: '' + host + '/api/product/getproduct?pid=' + item.pdt_id + '',
				type: 'get',
				dataType: 'json',
				success: function(data) {
					var id = "#pdt" + item.api_id + data.message.pdt_id;
					console.log("pdt:" + id);
					$(id).append(data.message.pdt_name)
				}
			})
		})
	},
});
//----点击删除
del = function(obj) {
	var pms = $(obj).attr("type");
	var obj = {
		"api_id": pms
	}
	console.log("数据对象" + pms);
	if (confirm("确认要删除吗？")) {
		window.event.returnValue = true;
	} else {
		window.event.returnValue = false;
	}
	if (window.event.returnValue == true) {
		$.ajax({
			url: '' + host + '/api/apiinfo/api',
			type: 'delete',
			dataType: 'json',
			contentType: 'application/json',
			data: JSON.stringify(obj),
			success: function(data) {
				alert("操作:" + data.title + ",\n结果:" + data.message);
				window.location.href = "api.html";
			},
		});
	}
}
//--添加操作
//查询产品列表
$.ajax({
	url: '' + host + '/api/product/getproductlist',
	type: 'get',
	dataType: 'json',
	success: function(data) {
		$.each(data.message, function(index, item) {
			/* console.log("数据对象：" + item.pdt_name); */
			var div = "";
			div = '<option id=' + item.pdt_id + '>' + item.pdt_name + '</option>';
			$("#productid").append(div)
		})
	}
});
//请求方式改变触发事件
$("#method").change(function() {
//var method = $("select id option:checked").attr("value");
  var method=$("#method").val();
	if(method){
		$("#upbody").html('VALUE')
	}
console.log("method:"+method);
})
//点击添加按钮
$('#btSearch').click(function() {
	var pdt_name = document.getElementById("productid").value;
	var pdt_id = $("select option:checked").attr("id");
	var api_name = document.getElementById("api_name").value;
	var method = document.getElementById("method").value;
	var url = document.getElementById("ApiUrl").value;
	var headerT = document.getElementById("ApiHeader").value;
					if(headerT.length!=0){
						var APIheader=JSON.parse(headerT);
						}else{var APIheader=headerT}
		 var API=$("#body").val();
		if(method=='get'||API.length==0){
			var APIbody=API;
		 }else{
				var APIbody=JSON.parse(API);
		 }
	var token = $("#havetoken").get(0).checked;
	if (token == true) {
		has_token = 1;
	} else {
		has_token = 0;
	}
if(method=='get'){
	var obj = {
		"api_name": api_name,
		"method": method,
		"header": APIheader,
		"body":"",
		"pdt_id": pdt_id,
		"values": APIbody,
		"url": url,
		"has_token": has_token
	};
}else{
	var obj = {
		"api_name": api_name,
		"method": method,
		"header": APIheader,
		"values":"",
		"pdt_id": pdt_id,
		"body": APIbody,
		"url": url,
		"has_token": has_token
	};
	}
  console.log("obj:"+JSON.stringify(obj));
	if (method.length == 0 || url.length == 0||pdt_id=='-1') {
		alert("某选项未选或未填写");
	} else {
		//上传字符串成功并跳转
		$.ajax({
		url: '' + host + '/api/apiinfo/api',
			type: 'post',
			dataType: 'json',
			contentType: 'application/json',
			data: JSON.stringify(obj),
			success: function(data) {
				alert("操作:" + data.title + ",\n结果:" + data.message);
				window.location.href = "api.html";
			}
		});
	}
});
/*--------修改API-----*/
//获取url中的参数
				function getUrlParam(name) {
					var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
					var r = window.location.search.substr(1).match(reg); //匹配目标参数
					if (r != null) return unescape(r[2]);
					return null; //返回参数值
				}
				//接收URL中的参数bId
				var id = getUrlParam('id');
				console.log('id:' + id);
				//根据aid获取api详情数据
				$.ajax({
					url: ''+host+'/api/apiinfo/api?aid='+id+'',
					type: 'get',
					dataType: 'json',
					success: function(data) {
						var msg = data.message;
						var body=msg.body;
						console.log("aa:"+body);
						console.log("aabb:"+JSON.stringify(msg.body));
						//回调数据
						$("#api_name").append('<input type="text" name="api_namename" id="api_nameid" value="' + msg.api_name + '">')
						$("#url").append('<textarea name="urlname" id="urlid"  cols="2" rows="2">'+msg.url+'</textarea>')
						$("#headerT").append('<textarea name="headername" id="headerTid"  cols="1" rows="1">'+JSON.stringify(msg.header)+'</textarea>')
						var method=msg.method;
						console.log('method1:'+method)
						$("select#method").val(method.toLowerCase());
						//获取method
						if(method=='get'){
							console.log('methodaaa:'+msg.values)
							$("#upbody").html('VALUE')
							$("#body").append('<textarea name="bodyname" id="bodyid"  cols="5" rows="10">'+msg.values+'</textarea>')
						}else{
							$("#body").append('<textarea name="bodyname" id="bodyid"  cols="5" rows="10">'+JSON.stringify(msg.body)+'</textarea>')
						}
						
						var token = msg.has_token;
              //回调是否存在token
						if (token == true) {
							/* console.log("ab:"+token); */
							document.getElementById("havetoken").checked = true
						} else {
							/* console.log("ab:"+token); */
							document.getElementById("havetoken").checked = false
						}
						var apdt_id = msg.pdt_id;
						console.log("a:" + apdt_id);
			    //获取产品列表
						$.ajax({
							url: ''+host+'/api/product/getproductlist',
							type: 'get',
							dataType: 'json',
							success: function(data) {
								$.each(data.message, function(index, item) {
									var div = "";
 									if(apdt_id==item.pdt_id){
										div = '<option id=' + item.pdt_id + ' value=' + item.pdt_id + ' selected>' + item.pdt_name + '</option>';
										$("#product").append(div)
										} else{
									div = '<option id=' + item.pdt_id + ' value=' + item.pdt_id + '>' + item.pdt_name + '</option>';
									//写入html属性id值为product中并显示
									$("#product").append(div)}
								})
							},
						});


					}
				});
				//点击修改，更新上传
				updateAPI = function() {
					var pdt_id = $("select option:checked").attr("id");
				  var method = document.getElementById("method").value;
					console.log("a:" + pdt_id);
					var api_name = document.getElementById("api_nameid").value;
					var body = document.getElementById("bodyid").value;
			if(method=='get'||body.length==0){
				var APIbody=body;
			 }else{
					var APIbody=JSON.parse(body);
			 }
					var headerT = document.getElementById("headerTid").value;
					console.log("aa123:"+headerT)
					if(headerT.length!=0){
						var APIheader=JSON.parse(headerT);
						}else{var APIheader=headerT}
					var url = document.getElementById("urlid").value;
					var token = $("#havetoken").get(0).checked;
					if (token == true) {
						has_token = 1;
					} else {
						has_token = 0;
					}
					//get请求上传value字段
					if(method=='get'){
			var obj = {
						"api_name": api_name,
						"method": method,
						"header": APIheader,
						"pdt_id": pdt_id,
						"values": APIbody,
						"body":"",
						"url": url,
						"has_token": has_token,
						"pdt_id": pdt_id,
						"api_id": id
					};
					}else{
			var obj = {
						"api_name": api_name,
						"method": method,
						"header": APIheader,
						"pdt_id": pdt_id,
						"body": APIbody,
						"values":"",
						"url": url,
						"has_token": has_token,
						"pdt_id": pdt_id,
						"api_id": id
					};
						}
					console.log("数据对象" + pdt_id);
					console.log('id:' + id);
					if (confirm("确认要修改吗？")) {
						window.event.returnValue = true;
					} else {
						window.event.returnValue = false;
					}
					if (window.event.returnValue == true) {
						$.ajax({
							url: ''+host+'/api/apiinfo/api',
							type: 'put',
							dataType: 'json',
							contentType: 'application/json',
							data: JSON.stringify(obj),
							success: function(data) {
								alert("操作:"+data.title+",\n结果:"+data.message);
								window.location.href = "api.html";
							},
						});
					}
				}
