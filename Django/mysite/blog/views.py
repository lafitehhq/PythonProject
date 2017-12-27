from django.shortcuts import render, HttpResponse

# Create your views here.

import datetime

def cur_time(request):
    # 示例一：返回字符串
    # return HttpResponse("<h1>测试返回成功</h1>")

    # 示例二：返回一个静态页面
    times = datetime.datetime.now()  # 获取当前的年月日时分
    return render(request, 'cur_time.html', {"abc": times})  # render方法用于渲染页面，底层调用的还是HttpResponse，第一个元素一定是request，第二个元素是html文件, abc接受一个变量

# 示例五：全局配置
    def introduce(req):
        return HttpResponse("测试全局配置成功")