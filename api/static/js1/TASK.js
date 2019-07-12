/* task展示列表 */
//获取展示数据并显示
				$.ajax({
					url: '' + host + '/api/taskinfo/tasklist',
					type: 'get',
					dataType: 'json',
					success: function(data) {
						$.each(data.message, function(index, item) {
							console.log("数据对象:" + item.task_name);
							var div = "";
							div = '<td>' + item.task_id + '</td>' +
								'<td>' + item.task_name + '</td>' +
								'<td><a href="#" onclick="addScript(this)" type="' +
								item.task_id + '"><img src="../static/img/Script.svg" class="g' + item.task_id +
								'"></a>&nbsp&nbsp&nbsp&nbsp<a href="config.html?id=' + item.task_id +
								'&name=' + item.task_name + '"><img src="../static/img/Settin.svg" class="h' + item.task_id +
								'"></a>&nbsp&nbsp&nbsp&nbsp<a href="#" id="dela1" class="b' + item.task_id +
								'" onclick="run(this)" type="' +
								item.task_id +
								'" ><img src="../static/img/run.svg" class="b' + item.task_id +
								'">&nbsp&nbsp&nbsp&nbsp<a href="#" id="dela1" class="c' +
								item.task_id + '" onclick="stop(this)" type="' +
								item.task_id + '" ><img src="../static/img/stop.svg" class="c' + item.task_id + '"></td>' +
								'<td><table width="100" border="0" cellspacing="0" cellpadding="0" align="center"><a href="#" id="dela1" class="a" onclick="del(this)" type="' +
								item.task_id + '" ><img src="../static/img/u48.svg">&nbsp&nbsp<a href="updatetask.html?id=' + item.task_id +
								'"><img src="../static/img/u50.svg" class="t"></a></td></table></td>';
							$("#tbody-result").append('<tr class="gradeX">' + div + '</tr>')
							//按钮的显示
							var c = ".c" + item.task_id; //停止图标
							var b = ".b" + item.task_id; //运行图标
							var h = ".h" + item.task_id; //locust配置图标
							var g = ".g" + item.task_id; //脚本生成
							if (item.task_status == true) {
								$(b).hide();
								$(h).hide();
								$(g).hide();
							} else {
								$(c).hide();
							}
							//$(b).show();
						})

					}
				});
				//点击执行生成脚本Script
				addScript = function(obj1) {
					var pms = $(obj1).attr("type");
					var obj1 = {
						"task_id": pms,
					}
					var run = '.b' + pms;
					var stop = '.c' + pms;
					var add = '.h' + pms;
					var script = '.g' + pms;
					if (confirm("确认要生成吗？")) {
						window.event.returnValue = true;
					} else {
						window.event.returnValue = false;
					}
					if (window.event.returnValue == true) {

						//显示运行按钮,locust按钮
						//执行生成脚本请求				
						$.ajax({
							url: '' + host + '/api/taskscript?task_id=' + pms + '',
							//url: 'http://192.168.1.56:8181/api/taskscript?task_id=' + pms + '',
							type: 'get',
							dataType: 'json',
							success: function(data) {
							if(data.status==200) {
								$(run).show();
								$(stop).hide();
								$(add).show();
								$(script).hide();
								alert("操作:" + data.title + ",\n结果:" + data.message);
							}else{
								$(run).show();
								$(stop).hide();
								$(add).show();
								$(script).show();
								alert("操作:" + data.title + ",\n结果:" + data.message);
							}
							},
						});
					}
				}
				//点击执行运行
				run = function(obj1) {
					var pms = $(obj1).attr("type");
					var obj1 = {
						"task_id": pms,
						"task_status": true
					}
					var run = '.b' + pms;
					var stop = '.c' + pms;
					var add = '.h' + pms;
					var script = '.g' + pms;
					console.log("statu:" + run);

					if (confirm("确认要执行吗？")) {
						window.event.returnValue = true;
					} else {
						window.event.returnValue = false;
					}
					if (window.event.returnValue == true) {

						//显示停止按钮
						//执行运行请求				
						$.ajax({
							url: '' + host + '/api/taskinfo/task?tid=' + pms + '',

							type: 'get',
							dataType: 'json',
							success: function(data) {
								var task_id = pms;
								var obj1 = {
									task_id: task_id,
									task_name: data.message.task_name,
									associated_case: data.message.associated_case,
									task_status: true
								}
								var locust = data.message.locust_cl;
								$.ajax({
									url: '' + host + '/api/taskinfo/task',
									type: 'put',
									dataType: 'json',
									contentType: 'application/json',
									data: JSON.stringify(obj1),
									success: function(data) {
										if (data.status == 201) {
											console.log("obj1：" + JSON.stringify(locust));
											$(run).hide();
											$(stop).show();
											$(add).hide();
											$(script).hide();
											//遍历locusst
											for (i = 0; i < locust.length; i++) {
												var str = locust[i].parameter;
												var reg = RegExp(/=/);
												var reg0 = RegExp(/--web-host/);
												var reg1 = RegExp(/--web-port/);
												var reg2 = RegExp(/--no-web/);
												if (str.match(reg0)) {
													arr = str.split("=");
													var webhost = arr[1];
												}
												if (str.match(reg1)) {
													arr = str.split("=");
													var webport = arr[1];
												}
												if (str.match(reg2)) {
													var noweb = true;
												} else {
													var noweb = false;
												}
											};
											console.log("webhost" + webhost);
											console.log("webport:" + webport);
											console.log("webport2:" + noweb);
											if (noweb == false) {
												weburl = 'http://' + webhost + ':' + webport;
												console.log("weburl:" + weburl);
												window.open(weburl);

											}
											//判断是否在运行中
											$.ajax({
												url: '' + checkhost + '/api/task/check-locust',
												type: 'get',
												dataType: 'json',
												success: function(data) {
												if (data.message==false) {
													//发送运行标识order
													$.ajax({
														url: '' + host + '/api/task-performance?order=1&task_id=' + pms + '',
														type: 'get',
														dataType: 'json',
														success: function(data) {
														},
                                                        error: function (XMLHttpRequest, textStatus, errorThrown) {
                                                            // 状态码
                                                            console.log(XMLHttpRequest.status);
                                                            // 状态
                                                            console.log(XMLHttpRequest.readyState);
                                                            // 错误信息
                                                            console.log(textStatus);
                                                            alert(textStatus+':'+XMLHttpRequest.status)
                                                            $(run).show();
                                                            $(stop).hide();
                                                            $(add).show();
                                                            $(script).show();

                                                        }
													})
												} else if(data.message==true) {
													alert('程序正在执行中');
													$(run).hide();
													$(stop).show();
													$(add).hide();
													$(script).hide();
												}else{
													alert('程序发生异常');
												}
												}
											},
											)
										}
									},
								});
							},
						});
					}
				}
				//点击停止运行
				stop = function(obj1) {
					var pms = $(obj1).attr("type");
					var obj1 = {
						"task_id": pms,
						"task_status": true
					}
					var run = '.b' + pms;
					var stop = '.c' + pms;
					var add = '.h' + pms;
					var script = '.g' + pms;
					console.log("statu:" + run);

					if (confirm("确认要停止吗？")) {
						window.event.returnValue = true;
					} else {
						window.event.returnValue = false;
					}
					if (window.event.returnValue == true) {
						//显示运行按钮
						//执行停止请求
						//判断是否执行
						$.ajax({
							url: '' + checkhost + '/api/task/check-locust',
							type: 'get',
							dataType: 'json',
							success: function(data) {
								if (data.message==true) {//发送运行标识order
						$.ajax({
							url: '' + host + '/api/taskinfo/task?tid=' + pms + '',
							type: 'get',
							dataType: 'json',
							success: function(data) {
								var task_id = pms;
								var obj1 = {
									task_id: task_id,
									task_name: data.message.task_name,
									associated_case: data.message.associated_case,
									task_status: false
								}
								console.log("obj1：" + JSON.stringify(obj1));
								$.ajax({
									url: '' + host + '/api/taskinfo/task',
									type: 'put',
									dataType: 'json',
									contentType: 'application/json',
									data: JSON.stringify(obj1),
									success: function(data) {
										$.ajax({
											url: '' + host + '/api/task-performance?order=0&task_id=' + pms + '',
											type: 'get',
											dataType: 'json',
											success: function(data) {
												if (data.status == 200) {
													$(stop).hide();
													$(run).show();
													$(add).show();
													$(script).show();
												} else {
													$(stop).hide();
													$(run).show();
													$(add).show();
													$(script).show();
												}
											},
                                            error: function (XMLHttpRequest, textStatus, errorThrown) {
                                                // 状态码
                                                console.log(XMLHttpRequest.status);
                                                // 状态
                                                console.log(XMLHttpRequest.readyState);
                                                // 错误信息
                                                console.log(textStatus);
                                                alert(textStatus+':'+XMLHttpRequest.status)
                                                $(run).hide();
                                                $(stop).show();
                                                $(add).hide();
                                                $(script).hide();

                                            }
										});

										//window.location.href="task.html"; 
									},
								});
							},
						});}else if(data.message==false){
                                   alert("程序未执行");
									$(stop).hide();
									$(run).show();
									$(add).show();
									$(script).show();
								}else{
									alert("程序有异常产生");
								}



							}})
					}
				}
				//点击删除
				del = function(obj) {
					var pms = $(obj).attr("type");
					var obj = {
						"task_id": pms
					}
					console.log("数据对象" + pms);
					if (confirm("确认要删除吗？")) {
						window.event.returnValue = true;
					} else {
						window.event.returnValue = false;
					}
					if (window.event.returnValue == true) {
						$.ajax({
							url: '' + host + '/api/taskinfo/task',
							type: 'delete',
							dataType: 'json',
							contentType: 'application/json',
							data: JSON.stringify(obj),
							success: function(data) {
								alert("操作:" + data.title + ",\n结果:" + data.message);
								window.location.href = "task.html";
							},
						});
					}
				}
//addtask
					$(function() {
						$.ajax({
							url: ''+host+'/api/caseinfo/caselist',
							type: 'get',
							dataType: 'json',
							success: function(data) {
								$.each(data.message, function(index, item) {
									var div = "";
									div='<tr ><td width="147" ><input type="checkbox" name="interest" id='+item.case_id+' value='+item.case_name+' class-="gcs-checkbox"><label style="width:300px">'+item.case_name+'</label></td></tr>';
									$("#caselist").append( div )
									/* canVote=true; */
								})
							}
						});

						updateTask = function() {
							var datalist=new Array();;//定义一个数组
							var flg=0;
							$('input[name="interest"]:checked').each(function(){
								/* var id1=id_array.push($(this).attr('id')); */
								/* var content = $("#"+id1 +).val(); */
								flg++;
								console.log("fla:"+flg);
								var case_id=$(this).attr('id');
								var case_name=$(this).attr('value');
								var obj=new Object();
								obj.case_id=case_id;
								obj.case_name=case_name;
								datalist.push(obj);
								console.log("weight_text1:"+JSON.stringify(datalist));
							});
							var task_name = document.getElementById("task_nameid").value;
							var arr1 = new Array();
							var dataobj = {
								"task_name": task_name,
								"associated_case":datalist,
								"locust_cl":arr1
							};
							console.log("dataobj:"+JSON.stringify(dataobj));
							if (confirm("确认要添加吗？")) {
								window.event.returnValue = true;
							} else {
								window.event.returnValue = false;
							}
							if (window.event.returnValue == true) {
								$.ajax({
									url: ''+host+'/api/taskinfo/task',
									type: 'post',
									dataType: 'json',
									contentType: 'application/json',
									data: JSON.stringify(dataobj),
									success: function(data) {
										alert("操作:"+data.title+",\n结果:"+data.message);
										window.location.href="task.html";
									},
								});
							}
						}

					});