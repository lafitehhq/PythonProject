from django.shortcuts import render, redirect

# Create your views here.

from app01 import models

# 1.定义登录初始页面
def login(req):
    # print(req.method)
    # 1.6.向用户表中插入数据
    # models.Administrator.objects.create(
    #     username='Vito',
    #     password='123456'
    # )

        # 1.4.初始化报错信息为空
    message = ""
    if req.method == "POST":
        # 1.1.获取用户输入的用户信息,注意：
        user = req.POST.get('user')
        pwd = req.POST.get('pwd')
        # 1.2.若输入的账户密码信息是（admin；admin123），则跳转至登录成功页面（index.html）
        # if user == 'admin' and pwd == 'admin123':
        # 1.5.读取数据库中的表用户信息
        c = models.Administrator.objects.filter(username=user, password=pwd).count()  # 获取用户名密码的个数
        if c:  # 若用户名密码存在则将输入的信息写入cookie
            rep = redirect('/index.html')
            rep.set_cookie('username', user)

            return rep
        # 1.3.若输入的账户密码信息不符，则跳转至初始登录页面，并返回报错信息
        else:
            message = "用户名或密码错误"
    return render(req, 'login.html', {'msg': message})

# 2.定义登录成功的跳转页面
def index(req):
    username = req.COOKIES.get('username')
    # 若用户登录则跳转至成功页面；否则返回原登录页面
    if username:
        return render(req, 'index.html', {'username': username})
    else:
        return redirect('/login.html')
