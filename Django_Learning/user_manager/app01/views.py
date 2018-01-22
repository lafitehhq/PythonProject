from django.shortcuts import render, redirect

# Create your views here.

from app01 import models

# #############################################登录版本1.0#############################################

# 1.定义cookie方式登录初始页面
# def login(req):
#     # print(req.method)
#     # 1.6.向用户表中插入数据
#     # models.Administrator.objects.create(
#     #     username='Vito',
#     #     password='123456'
#     # )
#
#         # 1.4.初始化报错信息为空
#     message = ""
#     if req.method == "POST":
#         # 1.1.获取用户输入的用户信息,注意：
#         user = req.POST.get('user')
#         pwd = req.POST.get('pwd')
#         # 1.2.若输入的账户密码信息是（admin；admin123），则跳转至登录成功页面（index.html）
#         # if user == 'admin' and pwd == 'admin123':
#         # 1.5.读取数据库中的表用户信息
#         c = models.Administrator.objects.filter(username=user, password=pwd).count()  # 获取用户名密码的个数
#         if c:  # 若用户名密码存在则将输入的信息写入cookie
#             rep = redirect('/index.html')
#         # 1.7.cookie的应用
#             # 普通版的cookie【不安全】
#             # rep.set_cookie('username', user, max_age=10)  # max_age=10表示失效时间是10s
#             # rep.set_cookie('password', pwd, max_age=10)  # max_age=10表示失效时间是10s
#             # 签名(加密)的cookie【安全】
#             rep.set_signed_cookie('username', user, max_age=10)
#             rep.set_signed_cookie('password', pwd, max_age=10)
#
#             return rep
#         # 1.3.若输入的账户密码信息不符，则跳转至初始登录页面，并返回报错信息
#         else:
#             message = "用户名或密码错误"
#     return render(req, 'login.html', {'msg': message})

# 2.定义cookie方式登录成功的跳转页面
# def index(req):
#     # 1.8.cookie的应用
#         # 获取普通版cookieh的设置
#     # username = req.COOKIES.get('username')
#         # 获取签名版cookie的设置
#     username = req.get_signed_cookie('username')
#     # 若用户登录则跳转至成功页面；否则返回原登录页面
#     if username:
#         return render(req, 'index.html', {'username': username})
#     else:
#         return redirect('/login.html')
# 3.客户端设置cookie的方法
# def js_cookie(req):
#     obj = render(req, 'js_cookie.html')
#     obj.set_cookie('Yanina', 'girl')
#     return obj

# #############################################登录版本2.0#############################################

# # 4.定义session方式登录初始页面
# def login_2(req):
#     message = ""
#     if req.method == "POST":
#         user = req.POST.get('user')
#         pwd = req.POST.get('pwd')
#
#         c = models.Administrator.objects.filter(username=user, password=pwd).count()
#         if c:
#             req.session['is_login'] = True
#             req.session['username'] = user
#             req.session['password'] = pwd
#             rep = redirect('/index_2.html?user='+ user)
#             return rep
#         else:
#             message = "用户名或密码错误"
#     obj = render(req, 'login_2.html', {'msg': message})
#     return obj
#
# # 5.定义session方式登录成功的跳转页面
# def index_2(req):
#     is_login = req.session.get('is_login')
#     if is_login:
#         current_user = req.session.get('username')
#         return render(req, 'index_2.html', {'username' : current_user})
#     else:
#         return redirect('/login_2.html')
#
# # 6.定义session方式注销初始页面
# def logout_2(req):
#     req.session.clear()
#     return redirect('/login_2.html')


# #############################################登录版本3.0#############################################

# def login(req):
#     message = ""
#     v = req.session
#     print(type(v))
#     from django.contrib.sessions.backends.db import SessionStore
#     if req.method == "POST":
#         user = req.POST.get('user')
#         pwd = req.POST.get('pwd')
#
#         c = models.Administrator.objects.filter(username=user, password=pwd).count()
#         if c:
#             req.session['is_login'] = True
#             req.session['username'] = user
#             rep = redirect('/index.html')
#             return rep
#         else:
#             message = "用户名或密码错误"
#     obj = render(req, 'login_3.html', {'msg': message})
#     return obj
#
# def logout(req):
#     req.session.clear()
#     return redirect('/login_3.html')
#
# # 10.装饰器实现代码复用
# def auth(func):
#     def inner(req, *args, **kwargs):
#         is_login = req.session.get('is_login')
#         if is_login:
#             return func(req, *args, **kwargs)
#         else:
#             return redirect('/login_3,html')
#     return inner
#
#
# # 11.登录函数
# @auth
# def index_3(req):
#     current_user = req.session.get('username')
#     return render(req, 'index_3.html', {'username': current_user})
#
# # 7.定义操作班级表
# @auth
# def handle_classes(req):
#     current_user = req.session.get('username')
#     return render(req, 'index_3.html', {'username': current_user})
#
# # 8.定义操作学生表
# @auth
# def handle_student(req):
#     current_user = req.session.get('username')
#     return render(req, 'student.html')
#
# # 9.定义操作教师表
# @auth
# def handle_teacher(req):
#     current_user = req.session.get('username')
#     return render(req, 'teacher.html')

def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login.html')
    return inner

@auth
def index(request):
    current_user = request.session.get('username')
    return render(request, 'index.html',{'username': current_user})

@auth
def handle_classes(request):

    current_user = request.session.get('username')
    return render(request, 'classes.html', {'username': current_user})


def handle_student(request):
    is_login = request.session.get('is_login')
    if is_login:
        current_user = request.session.get('username')
        return render(request, 'student.html', {'username': current_user})
    else:
        return redirect('/login.html')


def handle_teacher(request):
    is_login = request.session.get('is_login')
    if is_login:
        current_user = request.session.get('username')
        return render(request, 'teacher.html', {'username': current_user})
    else:
        return redirect('/login.html')



