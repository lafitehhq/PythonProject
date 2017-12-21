from django.shortcuts import render

# Create your views here.

# 示例一：提交数据并展示
# info_list = []
# def userInfor(req):
#     if req.method == "POST":
#         username = req.POST.get("username",None)
#         sex = req.POST.get("sex",None)
#         email = req.POST.get("email",None)
#
#         info = {"username": username, "sex": sex, "email": email}
#         info_list.append(info)
#     return render(req, "userInfor.html", {"info_list": info_list})


# 示例二：提交数据并展示(数据库)
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
            username=u,
            sex=s,
            email=e
        )
        info_list = models.UserInfor.objects.all()
        return render(req, "userInfor.html", {"info_list": info_list})
    return render(req, "userInfor.html")

