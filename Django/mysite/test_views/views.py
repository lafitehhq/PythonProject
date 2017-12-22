from django.shortcuts import render

# Create your views here.

user_list = []  # 创建一个空列表存放输入的客户数据

def userInfo(req):
    if req.method == 'POST':
        u = req.POST.get("username", None)  # 如果返回的值是字典有值，则返回键，否则返回None
        s = req.POST.get("sexual", None)  # username,sexual,email必须与index.html对应
        e = req.POST.get("email", None)
        # 示例一：
        # print("username", u)
        # print("sexual", s)
        # print("email", e)
        # 示例二：
        user = {"username": u, "sexual": s, "email": e}
        user_list.append(user)  # append()方法将字典存放入列表

        return render(req, "index.html", {"user_list": user_list})
    return render(req, "index.html")



# def login(req):
#     if req.method == "POST":
#         if 1:
#             # return redirect("/yuan_back/")
#             name = "yuanhao"
#             return render(req, "my backend.html", locals())
#     return render(req, "login.html", locals())
#
# def yuan_back(req):
#     name = "苑昊"
#     return render(req, "my backend.html", locals())