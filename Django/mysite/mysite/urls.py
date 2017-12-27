"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from blog import views as blog_views
from test_views import views as test_views_views
from test_database import views as test_database_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 全局路径配置，自动生成

# 01.Django学习之测试返回一个页面
    # 返回字符串/静态页面
    # url(r'^cur_time', blog_views.cur_time), # 打开浏览器连接：http://127.0.0.1:8080/cur_time

# 02.Django学习之视图函数
    # 示例一：提交数据并展示到控制台
    # url(r"userInfo", test_views_views.userInfo),  # 打开浏览器连接：http://127.0.0.1:8080/userInfo/，输入信息提交后会在控制台会显示输入信息
    # 示例二：settings的配置，读取文件夹中的静态文件
    # url(r"userInfo", test_views_views.userInfo),  # 同上
    # 示例三：
    # url(r'^articles/2003/$', test_views_views.totalmatch),  # 完全匹配：以articles/2003/全匹配；打开浏览器连接：http://127.0.0.1:8080/articles/2003/，显示totlmatch函数中的内容
    # url(r'^articles/[0-9]{4}/$', test_views_views.partialmatch_1),  # 部分匹配：以articles开头，以4位0-9组成的字符结尾的；打开浏览器连接：http://127.0.0.1:8080/articles/1992/，显示partialmatch_1函数中的内容
    # url(r'^articles/([0-9]{4})/$', test_views_views.partialmatch_2),  # 把url输入的路径参数（一个）传入到视图函数（在传入参数外用小括号括起来）：以articles开头，以4位0-9组成的字符结尾的；打开浏览器连接：http://127.0.0.1:8080/articles/1992/，显示partialmatch_2函数中的内容
    # url(r'^articles/([0-9]{4})/([0-9]{2})/$', test_views_views.partialmatch_3),  # # 把url输入的路径参数（两个）传入到视图函数（在传入参数外用小括号括起来）：以articles开头，以4位0-9组成的字符加以2位0-9组成的字符结尾的；打开浏览器连接：http://127.0.0.1:8080/articles/1992/07，显示partialmatch_3函数中的内容
    # url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', test_views_views.partialmatch_4),  # 同上，优化了views中传参必须按顺序的缺点，用?P<>为参数起别名；打开浏览器连接：http://127.0.0.1:8080/articles/1992/07，显示partialmatch_4函数中的内容
    # url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', test_views_views.article_detail),
    # 示例四：登录展示
    # url(r'^login', test_views_views.login_1, name='Vito'),  # 绝对路径法：前端html输入表单信息后跳转至HttpResponse展示页；打开浏览器连接：http://127.0.0.1:8080/login/，输入Vito 123提交后跳至登录成功提示
    # url(r'^pay/login', test_views_views.login_2, name='Yanina')  # 别名法：前端html输入表单信息后跳转至HttpResponse展示页；打开浏览器连接：http://127.0.0.1:8080/pay/login/，输入Vito 123提交后跳至登录成功提示
    # 示例五：路径分发
    url(r'^blog', include('blog.urls'))  #  在全局路径映射下映射blog中的app


# 03.Django学习之数据库
    # 控制台输入创建数据库：python3 manage.py makemigrations；python3 manage.py migrate。 db.sqlite3会生成test_database_userinfor的表
    # 示例一：提交数据后插入至数据库
    # url(r'^userInfor/', test_database_views.userInfor),  # 打开浏览器连接：http://127.0.0.1:8080/userInfor/，输入信息提交后会在控制台会显示输入,并且数据库会插入输入的数据
    # 示例二：前端展示所有的数据库信息
    # url(r'^userInfor/', test_database_views.userInfor),  # 同上


    # Django学习之视图函数
#     url(r"login", views.login),
#     url(r"yuan_back", views.yuan_back),

]





