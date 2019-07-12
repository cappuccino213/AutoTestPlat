$(function() {
    //搜索
    $.ajax({
        url: ''+host+'/api/product/getproductlist',
        type: 'get',
        dataType: 'json',
        success: function(data) {

            $.each(data.message, function(index, item) {
                /* alert(data); */
                //console.log("数据对象：" + data.desc);
                var div = "";
                div = '<td>' + item.pdt_id + '</td>' +
                    '<td>' + item.pdt_name + '</td>' +
                    '<td>' + item.version + '</td>' +
                    '<td >' + item.description + '</td>' +
                    '<td>' + item.host + '</td>' +
                    '<td><table width="100" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td><a href="#" id="dela1" onclick="del(this)" type="'+item.pdt_id+'" ><img src="../static/img/u48.svg"></td><td><a href="updateproduct.html?id='+item.pdt_id+'"><img src="../static/img/u50.svg"></a></td></tr></table></td></tr>';
                $("#tbody-result").append('<tr class="gradeX">' + div + '</tr>')
            })
        }
    });
    //点击删除
    del=function(obj) {
        var pms=$(obj).attr("type");
        var obj={"pdt_id":pms}
        console.log("数据对象" + pms);
        if (confirm("确认要删除吗？")) {
            window.event.returnValue = true;
        } else {
            window.event.returnValue = false;
        }
        if (window.event.returnValue == true) {
            $.ajax({
                url: ''+host+'/api/product/delproduct',
                type: 'delete',
                dataType: 'json',
                contentType: 'application/json',
                data:JSON.stringify(obj),
                success: function(data) {
                    alert("操作:"+data.title+",\n结果:"+data.message);
                    window.location.href="index.html";
                },
            });
        }
    }
});
//js读取本地文件
function upload(input) {
    //支持chrome IE10
    $('#addapi_json').html("");
    if (window.FileReader) {
        var file = input.files[0];
        filename = file.name.split(".")[0];
        var reader = new FileReader();
        reader.onload = function() {
            console.log("1:"+this.result);
            api_json=this.result;
            var div = "";
            div = '<textarea name="description" id="api_json" cols="45" rows="5">'+api_json+'</textarea>';
            $("#addapi_json").append(div);
        }
        reader.readAsText(file);


    }
    //支持IE 7 8 9 10
    else if (typeof window.ActiveXObject != 'undefined'){
        var xmlDoc;
        xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
        xmlDoc.async = false;
        xmlDoc.load(input.value);
        console.log("2:"+xmlDoc.xml);
    }
    //支持FF
    else if (document.implementation && document.implementation.createDocument) {
        var xmlDoc;
        xmlDoc = document.implementation.createDocument("", "", null);
        xmlDoc.async = false;
        xmlDoc.load(input.value);
        console.log("3:"+xmlDoc.xml);
    } else {
        alert('error');
    }
}
$(function() {
    $('#btSearch').click(function() {
        var description = $('#description').val();
        var host1 = $('#host').val();
        var pdt_name = $('#pdt_name').val();
        var version = $('#version').val();
        var api_json = $('#api_json').val();
        /* console.log("13:"+host); */
        var obj = {
            "description":description,
            "host":host1,
            "pdt_name":pdt_name,
            "version":version,
            "api_json":JSON.parse(api_json),
            //"delete_flag":"0"
        };
         console.log("obj:"+JSON.stringify(obj));
        if(pdt_name.length==0||version.length==0||description.length==0||host1.length==0){
            alert("某选项未填写,请填写完整");
        }else{
            /*              alert(obj); */
            $.ajax({
                url:''+host+'/api/product/addproducts',
                type:'post',
                dataType:'json',
                contentType:'application/json',
                data:JSON.stringify(obj),
                success: function(data) {
                    alert("操作:"+data.title+",\n结果:"+data.message);
                    window.location.href="index.html";
                },
                error:function(data){
                    alert(data.status);
                }
            });}
    });
});
