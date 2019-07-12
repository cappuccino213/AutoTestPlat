//----添加case
//获取产品列表
$.ajax({
	url: '' + host + '/api/product/getproductlist',
	type: 'get',
	dataType: 'json',
	success: function(data) {
		$.each(data.message, function(index, item) {
			/* console.log("数据对象：" + item.pdt_name); */
			var div = "";
			div = '<option id=' + item.pdt_id + ' value=' + item.pdt_id + '>' + item.pdt_name + '</option>';
			$("#product").append(div)
		})
	}
});
var pdt_id = $("select option:checked").attr("id");
if (pdt_id == "-1") {
	$("#apilistone").hide();
	$("#apilisttwo").show();
}
console.log("a:" + pdt_id);
$("#product").change(function() {
	var pdt_id = $("select option:checked").attr("id");
	if (pdt_id != "-1") {
		$("#apilistone").show();
		$("#apilisttwo").hide();
	} else {
		$("#apilistone").hide();
		$("#apilisttwo").show();
	}
	console.log("pdt_id:" + pdt_id);
	$("#apilistone").html("");
	//根据pdt_id获取对应产品的API列表
	$.ajax({
		url: '' + host + '/api/apiinfo/api?pid=' + pdt_id + '',
		type: 'get',
		dataType: 'json',
		success: function(data) {
			$.each(data.message, function(index, item) {
				var div = "";
				div = '<table width="287" border="1"><tr><td width="147"><input type="checkbox" name="interest" id=' + item.api_id +
					' value=' + item.api_name + ' class-="gcs-checkbox"><label style="width:300px">' + item.api_name +
					'</label></td><td width="124"><table width="10" border="1"><tr><td width="14">权重</td><td width="20"><input type="text" name="weight" id=nme' +
					item.api_id + '></td></tr></table></td></tr></table>';
				$("#apilistone").append(div)
				/* canVote=true; */
			})
		}
	});

});
//添加CASE
updateproduct = function() {
	var datalist = new Array();; //定义一个数组 
	var flg = 0;
	//遍历获取勾选状态下的id值
	$('input[name="interest"]:checked').each(function() {
		var id1 = $(this).attr('id');
		console.log("复选框id:" + $(this).attr('value'));
		var id2 = "nme" + id1;
		console.log("weight_idname:" + id2);
		var weight = document.getElementById(id2).value;
		if (weight.length == 0) {
			alert("请输入" + $(this).attr('value') + "权重值");
			flg = 1;
		}
		console.log("weight_text:" + weight);
		var obj = new Object();
		obj.api_id = id1;
		obj.weight = weight;
		datalist.push(obj);
		console.log("weight_text1:" + JSON.stringify(datalist));

	});
	var case_name = document.getElementById("case_nameid").value;
	var dataobj = {
		"case_name": case_name,
		"api_weight": datalist
	};
	//条件判断
	if (case_name.length == 0) {
		alert("请输入CASE名称");
	} else {
		if (flg == 0) {
			console.log("dataobj:" + JSON.stringify(dataobj));
			if (confirm("确认要添加吗？")) {
				window.event.returnValue = true;
			} else {
				window.event.returnValue = false;
			}
			if (window.event.returnValue == true) {
				$.ajax({
					url: '' + host + '/api/caseinfo/case',
					type: 'post',
					dataType: 'json',
					contentType: 'application/json',
					data: JSON.stringify(dataobj),
					success: function(data) {
						alert("操作:" + data.title + ",\n结果:" + data.message);
						window.location.href = "case.html";
					},
				});
			}
		}
	}
}
// ------case列表显示
//展示case列表
$.ajax({
	url: '' + host + '/api/caseinfo/caselist',
	type: 'get',
	dataType: 'json',
	success: function(data) {
		$.each(data.message, function(index, item) {
			/* 	console.log("数据对象：" + data.desc); */
			var div = "";
			div = '<td>' + item.case_id + '</td>' +
				'<td>' + item.case_name + '</td>' +
				'<td><table width="100" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td><a href="#" id="dela1" onclick="del(this)" type="' +
				item.case_id + '" ><img src="../static/img/u48.svg"></td><td><a href="updatecase.html?id=' + item.case_id +
				'"><img src="../static/img/u50.svg"></a></td></tr></table></td></tr>';
			$("#tbody-result").append('<tr class="gradeX">' + div + '</tr>')
		})
	}
});
//点击删除
del = function(obj) {
var pms = $(obj).attr("type");
var obj = {
	"case_id": pms
}
console.log("数据对象" + pms);
if (confirm("确认要删除吗？")) {
	window.event.returnValue = true;
} else {
	window.event.returnValue = false;
}
if (window.event.returnValue == true) {
	$.ajax({
		url: '' + host + '/api/caseinfo/case',
		type: 'delete',
		dataType: 'json',
		contentType: 'application/json',
		data: JSON.stringify(obj),
		success: function(data) {
			alert("操作:" + data.title + ",\n结果:" + data.message);
			window.location.href = "case.html";
		},
	});
}
}

