function GetData(ip){
    //var url = "http://192.168.31.85:9001/api/json?tree=jobs"
    var url = "/apitest/"+ ip
    var httpRequest  = new XMLHttpRequest();
    httpRequest.open("GET", url);
    // httpRequest.setRequestHeader("Content-type", "text/html");
    // httpRequest.setRequestHeader("Access-Control-Allow-Origin","*");
    httpRequest.send();
    // setTimeout('location.reload()',1000);
    //
    httpRequest.onreadystatechange = function () {
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {
                var json = httpRequest.responseText;//获取到json字符串，还需解析
                console.log(json);
            }
    };
}

function PostData(ip){
    var r = confirm("是否确定要重启");
	if (r)
	{
		var url = "/apitest/"+ ip
        var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
        httpRequest.open('POST', url, true); //第二步：打开连接
        httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
        httpRequest.send('name=teswe&ee=ef');//发送请求 将情头体写在send中
        /**
         * 获取数据后的处理程序
         */
        httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {//验证请求是否发送成功
                var json = httpRequest.responseText;//获取到服务端返回的数据
                console.log(json);
            }
        };
        alert("更新成功")
	}

}



