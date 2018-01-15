1. 基于JS的Ajax的实现
1.1.XMLHttpRequest对象的5种状态：
    0：初始化未完成状态，只是创建了XMLHttpRequest对象，还未调用open()方法；
    1：请求已开始，open()方法已调用，但还没调用send()方法；
    2：请求发送完成状态，send()方法已调用；
    3：开始读取服务器响应；
    4：读取服务器响应结束。
1.2.基于JS的Ajax的实现步骤
    步骤1： 定义XMLHttpRequest对象的创建函数
    步骤2：
        var xmlhttp = XMLHttprequest()
    步骤3：连接数据库
        xmlhttp.open("")
    步骤4：实例化XMLHttprequest对象
        xmlhttp.send("name=alex")  # 请求体的内容if GET请求 : send(null)
    步骤5： 监听：xmlHttp（if == 4:{var context=xmlhttp.responsetext})



2. JSON与JSONP

3. 基于jquery的Ajax的实现
    $.ajax()