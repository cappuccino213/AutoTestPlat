//report列表展示
		$(function() {
			//搜索
					$.ajax({
						url: ''+host+'/api/reportinfo/reportlist',
						type: 'get',
						dataType: 'json',
						success: function(data) {
							$.each(data.message, function(index, item) {
								/* alert(data); */
								console.log("数据对象：" + data.desc);
								var div = "";
								div = '<td>' + item.rpt_id + '</td>' +
									'<td>' + item.report_name + '</td>' +
									'<td>' + item.case_id + '</td>' +
									'<td>' + item.create_date + '</td>' +
									'<td><a href="#" id="dela1" onclick="del(this)" type="'+item.rpt_id+'" ><img src="../static/img/u739.svg"></td>';
								$("#tbody-result").append('<tr class="gradeX">' + div + '</tr>')
							})
						}
			});
		//点击查看报告
		del=function(obj) {
			var pms=$(obj).attr("type");
			 var obj={"pdt_id":pms}
			  console.log("数据对象" + pms);
					$.ajax({
						url: ''+host+'/api/reportinfo/report?rid='+pms+'',
						//url: '192.168.1.56:8181/api/reportinfo/report?rpt_id=1',
						type: 'get',
						dataType: 'json',
/* 						contentType: 'application/json', 
						data:JSON.stringify(obj), */
						success: function(data) {
							//var filepath=data.message.file_path;
							console.log("file:"+data.message.file_path);
							var host1=''+host+'/viewreport/'+data.message.file_path+'';
							console.log("file:"+host1);
							window.open(host1);
							 //window.location.href="index.html"; 
						},
					});
				
			}
		});
