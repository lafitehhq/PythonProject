from django.shortcuts import render

# Create your views here.

# 提交数据并展示(数据库)
from test_database import models
def userInfor(req):
    if req.method == "POST":
        u = req.POST.get("username", None)
        s = req.POST.get("sex", None)
        e = req.POST.get("email", None)
        #  示例一：-----向数据库中插入数据-----
        models.UserInfor.objects.create(
            username=u,  # 将插入username字段
            sex=s,
            email=e
        )
        #  示例二：-----向数据库中插入数据后并把数据展示之前端-----
        info_list = models.UserInfor.objects.all()
        return render(req, "userInfor.html", {"info_list": info_list})
    return render(req, "userInfor.html")

