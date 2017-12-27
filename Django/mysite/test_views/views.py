from django.shortcuts import render, HttpResponse

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
        # return render(req, "index.html")
        # 示例二：
        user = {"username": u, "sexual": s, "email": e}
        user_list.append(user)  # append()方法将字典存放入列表
    return render(req, "index.html", {"user_list": user_list})

# 示例三：
    # 测试url全匹配
def totalmatch(req):
    return HttpResponse("测试-url全匹配")
    # 测试url条件匹配
def partialmatch_1(req):
    return HttpResponse("测试-url条件匹配")
    # 测试url路径参数(一个)传入到视图函数
def partialmatch_2(req, y):
    return HttpResponse("路径参数"+y+"传入到视图函数")
    # 测试url路径参数（两个）传入到视图函数
def partialmatch_3(req, y, m):
    return HttpResponse(y + "年" + m + "月")
    # 测试url路径参数（两个）传入到视图函数升级版
def partialmatch_4(req, year, month):
    return HttpResponse(month + "月" + year + "年")

# 示例四：登录跳转
    # 测试登录提交表单页面并跳转，在前端html中可以设置指定具体的url或含有某参数的url
def login_1(req):
    if req.method == "POST":
        name = req.POST.get('username')
        pwd = req.POST.get('userpassword')
        if name == 'Vito' and pwd == '123':
            return HttpResponse("登录成功")  # 如果信息符合则跳转该提示
        else:
            return HttpResponse("账号密码错误，请重新登录")
    return render(req, 'login.html')

def login_2(req):
    if req.method == "POST":
        name = req.POST.get('username')
        pwd = req.POST.get('userpassword')
        if name == 'Yanina' and pwd == '123':
            return HttpResponse("登录成功")  # 如果信息符合则跳转该提示
        else:
            return HttpResponse("账号密码错误，请重新登录")
    return render(req, 'login.html')

# 示例五：全局配置
    def introduce(req):
        return HttpResponse("测试全局配置成功")







    #     if 1:
    #         # return redirect("/yuan_back/")
    #         name = "yuanhao"
    #         return render(req, "my backend.html", locals())
    # return render(req, "login.html", locals())

# def yuan_back(req):
#     name = "苑昊"
#     return render(req, "my backend.html", locals())