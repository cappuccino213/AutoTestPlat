//-------展示api列表
var flag = 0;
$.ajax({
	url: '' + host + '/api/apiinfo/apilist',
	type: 'get',
	dataType: 'json',
	success: function(data) {
		$.each(data.message, function(index, item) {
			var div = "";
			div = '<td>' + item.api_name + '</td>' +
				'<td>' + item.method + '</td>' +
				'<td id="pdt' + item.api_id + '' + item.pdt_id + '"></td>' +
				'<td><table width="100" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td><a href="#" id="dela1" onclick="del(this)" type="' +
				item.api_id + '" ><img src="../static/img/u48.svg"></td><td><a href="updateapi.html?id=' + item.api_id +
				'"><img src="../static/img/u50.svg"></a></td></tr></table></td></tr>';
			$("#tbody-result").append('<tr id="tr' + item.pdt_id + '">' + div + '</tr>')
			$.ajax({
				url: '' + host + '/api/product/getproduct?pid=' + item.pdt_id + '',
				type: 'get',
				dataType: 'json',
				success: function(data) {
					var id = "#pdt" + item.api_id + data.message.pdt_id;
					//console.log("pdt:" + id);
					$(id).append(data.message.pdt_name)
				}
			})
		})
	},
});
$("#pro").change(function(){
	var pro=$("#pro").val();
	console.log("pro：" + pro);
	console.log("pro2：" + arr);
	$('#tbody-result tr').each(function(i){
	var parents=$(this).parent().parent().attr("id")
		console.log("trid23:"+parents);
		//$("#tr94").hide();
	})
	for(var i=0;i<arr.length;i++){
		if(pro==arr[i]){
		}else{
			var trid="#tr"+arr[i];
			//$(trid).hide();
			console.log("trid2:"+trid);
/*			for(n=0;n<te.length;n++)
			{
				if(te[n].style.display=="")
					te[n].style.display="none";
				else te[n].style.display="";
			}*/
		}
	}

})

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
var arr=[];//产品id数组
//--添加操作
//查询产品列表
$.ajax({
	url: '' + host + '/api/product/getproductlist',
	type: 'get',
	//async:false,
	dataType: 'json',
	success: function(data) {
		$.each(data.message, function(index, item) {
			/* console.log("数据对象：" + item.pdt_name); */
			var div = "";
			div = '<option value=' + item.pdt_id + '>' + item.pdt_name + '</option>';
			$("#productid").append(div)
			$("#pro").append(div)
			if(arr.indexOf(item.pdt_id)==-1){
				arr.push(item.pdt_id);
			}
		})
		console.log("产品id数组1:"+arr);
		return arr;
	}
});
console.log("产品id数组2:"+arr);
//单个产品触发事件
$("#productid").change(function() {
	var productid=$("#productid").val();
	console.log("productid1:"+productid);
//查询单个产品
$.ajax({
	url: ''+host+'/api/product/getproduct?pid=' +productid+ '',
	type: 'get',
	dataType: 'json',
	success: function(data) {
		var msg=data.message;
		var apiarray=msg.api_json;
		//去重
		//遍历数据；双层循环，外循环表示从0到arr.length，内循环表示从i+1到arr.length
		// 将没重复的右边值放入新数组。（检测到有重复值时终止当前循环同时进入外层循环的下一轮判断）
		var hash=[];
		for (var i = 0; i <apiarray.length; i++) {
			for (var j = i+1; j < apiarray.length; j++) {
				if(apiarray[i].function===apiarray[j].function){
					++i;
				}
			}
			hash.push(apiarray[i].function);
		}
		$('#functionid').html("");
		$("#functionid").append('<option id="-2" value="请选择模块">请选择模块</option>')
		for (var i = 0; i <hash.length; i++) {
			var div = "";
			div = '<option value=' + hash[i]+ '>'+i+','+ hash[i] + '</option>';
			$("#functionid").append(div)
		}
		console.log("hash:"+JSON.stringify(hash));
		//function--模块改变事件
		$("#functionid").change(function() {
			$('#apiid').html("");
			$("#apiid").append('<option id="-3" value="请选择接口">请选择API</option>')
			var  functionid = $("#functionid").val();
			//console.log("function:" + functionid);
			//console.log("apiarray:"+JSON.stringify(apiarray));
			for (i = 0; i < apiarray.length; i++) {
				//console.log("i："+apiarray.length)
				if(apiarray[i].function==functionid){
					console.log("function2："+apiarray[i].function);
					//console.log("function3："+functionid);
					var div = "";
					//div= '<option value=' +apiarray[i].uri + '>'+i+','+ apiarray[i].summary + '</option>';
					div= '<option >'+ apiarray[i].summary + '</option>';
					$("#apiid").append(div)}
			}
		})
		//summary--API名称改变事件
		$("#apiid").change(function() {
			$('#apiurl').html("");
			$('#ApiHeader1').html("");
			$('#addbody').html("");
			//$('#methodc').html("");
			//var productid = $("select option:checked").attr("id");
			var  arraryid = $("#apiid").val();
			console.log("apiarrayid:"+arraryid);

			for (i = 0; i < apiarray.length; i++) {
				//console.log("i："+apiarray.length)
				//console.log("function2："+apiarray[i].url);
				//console.log("apiarray['+arraryid+'].url："+apiarray[arraryid].uri);
				if (apiarray[i].summary == arraryid) {
					var div = "";
					div = '<input type="text" id="apiurl1" name="name2" value='+ apiarray[i].uri + '>';
					$("#apiurl").append(div)
					var div1 = "";
					div1 = '<textarea name="textarea" id="ApiHeader" cols="45" rows="3">'+JSON.stringify(apiarray[i].produces)+'</textarea>';
					$("#ApiHeader1").append(div1)
					var str=JSON.stringify(apiarray[i].produces);
					var reg = RegExp(/octet-stream/);
					if(str.match(reg)) {
						$('#proto_messagename').html("");
						var div3 = "";
						div3 = '<td>proto_message</td><td><input type="text" id="proto_message" value=' + JSON.stringify(apiarray[i].message) + ' ></td>';
						$("#proto_messagename").append(div3);

						$('#proto_filename').html("");
						var div4 = "";
						div4 = '<td>proto_file</td><td><input type="text" id="proto_file" value=' + apiarray[i].input_proto + ' ></td>';
						$("#proto_filename").append(div4);
						onsole.log("reg1:"+str)
					}else{
						console.log("reg2:"+str)
					}

					var div2 = "";
					div2 = '<textarea name="textarea2" id="body" cols="45" rows="5" >'+ JSON.stringify(apiarray[i].parameters) + '</textarea>';
					$("#addbody").append(div2);
					$("select#methodc").val(apiarray[i].method.toLowerCase());
						if(apiarray[i].method.toLowerCase()=='get'){
		$("#upbody").html('VALUE')
	}else{
		$("#upbody").html('BODY')}

				}
			}

		})

	}
});
})
//请求方式改变触发事件
$("#methodc").change(function() {
//var method = $("select id option:checked").attr("value");
  var methodc=$("#methodc").val();
	if(methodc=='get'){
		$("#upbody").html('VALUE')
	}else{
		$("#upbody").html('BODY')}
console.log("method1:"+methodc);
})



//点击添加按钮
$('#btSearch').click(function() {
	//var pdt_name = document.getElementById("productid").value;
	//var pdt_id = $("select option:selected").attr("id");
	var pdt_id =$("#productid").val();
	console.log("pdt_id:"+pdt_id);
	var api_name=$("#apiid").val();
	//var api_name = document.getElementById("apiid").value;
	console.log("api_name:"+api_name);
	var method = document.getElementById("methodc").value;
	var url=$("#apiurl1").val();
    var proto_message=$("#proto_message").val();
    var proto_file=$("#proto_file").val();
	console.log("url:"+proto_file);
	//var url = document.getElementById("apiurl").value;
	//var headerT = document.getElementById("ApiHeader").value;
	var headerT=$("#ApiHeader").val().toLowerCase();
		if(headerT.length!=0){
						var APIheader=JSON.parse(headerT);
						}else{var APIheader=headerT}
		console.log("header:"+headerT);
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
		"has_token": has_token,
        "proto_message":proto_message,
        "proto_file":proto_file
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
		"has_token": has_token,
        "proto_message":proto_message,
        "proto_file":proto_file
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
						$("#headerT").append('<textarea name="headername" id="headerTid" cols="45" rows="3" >'+JSON.stringify(msg.header).toLowerCase()+'</textarea>')
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
						var str=JSON.stringify(msg.header);
						var reg = RegExp(/octet-stream/);
						if(str.match(reg)){
							$('#proto_messagename').html("");
							var div3 = "";
							div3 = '<td>proto_message</td><td><input type="text" id="proto_message" value=' + msg.proto_message + ' ></td>';
							$("#proto_messagename").append(div3);

							$('#proto_filename').html("");
							var div4 = "";
							div4 = '<td>proto_file</td><td><input type="text" id="proto_file" value=' + msg.proto_file+ ' ></td>';
							$("#proto_filename").append(div4);
						}else{
							console.log("reg2:"+str)
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
                    var proto_message=$("#proto_message").val();
                    var proto_file=$("#proto_file").val();
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
						"api_id": id,
                "proto_message":proto_message,
                "proto_file":proto_file
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
						"api_id": id,
                "proto_message":proto_message,
                "proto_file":proto_file
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
