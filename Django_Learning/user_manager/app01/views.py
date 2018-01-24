from django.shortcuts import render, redirect,HttpResponse

# Create your views here.

from app01 import models

# #############################################登录版本1.0：cookie方式登录#############################################

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

# #############################################登录版本2.0：session方式登录#############################################

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


# #############################################登录版本3.0:使用装饰器+session#############################################

# # 7.定义session方式登录初始页面
# def login_3(req):
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
#             rep = redirect('/index_3.html?user='+ user)
#             return rep
#         else:
#             message = "用户名或密码错误"
#     obj = render(req, 'login_3.html', {'msg': message})
#     return obj
#
# # 8.定义session方式注销初始页面
# def logout_3(req):
#     req.session.clear()
#     return redirect('/login_3.html')
#
# # # 9.定义session方式登录成功的跳转页面
# # def index_3(req):
# #     is_login = req.session.get('is_login')
# #     if is_login:
# #         current_user = req.session.get('username')
# #         return render(req, 'index_3.html', {'username': current_user})
# #     else:
# #         return redirect('/login_3.html')
#
# # 10.操作前端的每个班级，学生，老师表
# # def handle_classes(req):
# #     # 10.1.登录认证的重复代码
# #     is_login = req.session.get('is_login')
# #     if is_login:
# #         current_user = req.session.get('username')
# #         return render(req, 'index_3.html', {'username': current_user})
# #     else:
# #         return redirect('/login_3.html')
# #     # 10.2.跳转至对应的html
# #     return render(req, 'classes.html')
# #
# # def handle_student(req):
# #     return render(req, 'student.html')
# #
# # def handle_teacher(req):
# #     return render(req, 'teacher.html')
#
# # 11.定义装饰器函数
# # # 11.1.装饰器函数模板
# # def auth(func):
# #     def inner(*args, **kwargs):
# #         return func()
# #     return inner  # 注意：inner不用加括号
#
# # 11.2.定义登录验证装饰器
# def auth(func):
#     def inner(req, *args, **kwargs):
#         # 获取session
#         is_login = req.session.get('is_login')
#         # 若登录成功(session存在)，执行func
#         if is_login:
#             return func(req, *args, **kwargs)
#         # 若登陆失败，返回登录页面
#         else:
#             return redirect('/login_3.html')
#     return inner
#
#
# # 12.定义session + 装饰器的方式登录成功的跳转页面
# @auth
# def index_3(req):
#     current_user = req.session.get('username')
#     return render(req, 'index_3.html', {'username': current_user})
#
# @auth
# def handle_classes(req):
#     current_user = req.session.get('username')
#     return render(req, 'classes.html', {'username': current_user})
#
# @auth
# def handle_student(req):
#     current_user = req.session.get('username')
#     return render(req, 'student.html', {'username': current_user})
#
# @auth
# def handle_teacher(req):
#     current_user = req.session.get('username')
#     return render(req, 'teacher.html', {'username': current_user})


# #############################################登录版本4.0:CBV方式#############################################
# from django import views
# from django.utils.decorators import method_decorator
#
# def outer(func):
#     def inner(req, *args, **kwargs):
#         print(req.method)
#         return func(req, *args, **kwargs)
#     return inner
#
# class Login(views.View):
#
#     # GET方法，获取的是空字符串
#     @method_decorator(outer)
#     def get(self, req, *args, **kwargs):
#         return render(req, 'login_3.html', {{'msg': ''}})
#
#     # POST方法
#     @method_decorator(outer)
#     def post(self, req, *args, **kwargs):
#         # 获取的是提交的信息
#         user = req.POST.get('user')
#         pwd = req.POST.get('pwd')
#         # 到数据库检测时候有账户
#         c = models.Administrator.objects.filter(username=user, password=pwd).count()
#         # 若存在用户信息,返回信息并跳转至index_3页面
#         if c:
#             req.session['is_login'] = True
#             req.session['username'] = user
#             rep = redirect('/index_3.html')
#         # 若不存在账户信息
#         else:
#             message = "用户名或密码错误"
#             return render(req, 'login_3.html', {{'msg': ''}})

# # #############################################登录版本5.0:CBV方式#############################################
# from django import views
#
# class Login_3(views.View):
#     def dispatch(self, req, *args, **kwargs):
#         if req.method == 'GET':
#             return HttpResponse('滚蛋')
#         # 调用父类的dispatch方法
#         ret  = super(Login, self).dispatch(req, *args, **kwargs)
#         print(111)
#         return ret
#
#     def get(self, req, *args, **kwargs):
#         print('GET')
#         return render(req, 'login_3.html', {{'msg : '''}})
#
#     def post(self, req, *args, **kwargs):
#         # 获取的是提交的信息
#         user = req.POST.get('user')
#         pwd = req.POST.get('pwd')
#         # 到数据库检测时候有账户
#         c = models.Administrator.objects.filter(username=user, password=pwd).count()
#         # 若存在用户信息,返回信息并跳转至index_3页面
#         if c:
#             req.session['is_login'] = True
#             req.session['username'] = user
#             rep = redirect('/index_3.html')
#         # 若不存在账户信息
#         else:
#             message = "用户名或密码错误"
#             return render(req, 'login_3.html', {{'msg': ''}})

# ##############################################登录版本5.0:CBV方式#############################################
from django import views
from django.utils.decorators import method_decorator

def outer(func):
    def inner(req, *args, **kwargs):
        print(req.method)
        return func(req, *args, **kwargs)
    return inner

@method_decorator(outer, name='dispatch')
class Login_3(views.View):
    def dispatch(self, req, *args, **kwargs):
        if req.method == 'GET':
            return HttpResponse('滚蛋')
        # 调用父类的dispatch方法
        ret  = super(Login, self).dispatch(req, *args, **kwargs)
        print(111)
        return ret

    def get(self, req, *args, **kwargs):
        print('GET')
        return render(req, 'login_3.html', {{'msg : '''}})

    def post(self, req, *args, **kwargs):
        # 获取的是提交的信息
        user = req.POST.get('user')
        pwd = req.POST.get('pwd')
        # 到数据库检测时候有账户
        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        # 若存在用户信息,返回信息并跳转至index_3页面
        if c:
            req.session['is_login'] = True
            req.session['username'] = user
            rep = redirect('/index_3.html')
        # 若不存在账户信息
        else:
            message = "用户名或密码错误"
            return render(req, 'login_3.html', {{'msg': ''}})





