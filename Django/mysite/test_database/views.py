from django.shortcuts import render

# Create your views here.

# 提交数据并展示(数据库)
from test_database import models
def userInfor(req):
    if req.method == "POST":
        u = req.POST.get("username", None)
        s = req.POST.get("sex", None)
        e = req.POST.get("email", None)
       #---------表中插入数据方式一
            # info={"username":u,"sex":e,"email":e}
            # models.UserInfor.objects.create(**info)
       #---------表中插入数据方式二
        models.UserInfor.objects.create(
            username=u,  # 将插入username字段
            sex=s,
            email=e
        )
        info_list = models.UserInfor.objects.all()
        return render(req, "userInfor.html", {"info_list": info_list})
    return render(req, "userInfor.html")

