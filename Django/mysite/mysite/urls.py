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
from django.conf.urls import url
from django.contrib import admin

from blog import views as blog_views
from test_views import views as test_views_views
from test_database import views as test_database_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

# 01.Django学习之测试返回一个页面
    # 返回字符串/静态页面
    # url(r'^cur_time', blog_views.cur_time), # 打开浏览器连接：http://127.0.0.1:8080/cur_time

# 02.Django学习之视图函数
    # 示例一：提交数据并展示到控制台
    # url(r"userInfo", test_views_views.userInfo),  # 打开浏览器连接：http://127.0.0.1:8080/userInfo/，输入信息提交后会在控制台会显示输入信息
    # 示例二：提交数据并展示到前端
    # url(r'^userInfor/', test_database_views.userInfor),  # 打开浏览器连接：http://127.0.0.1:8080/userInfo/，输入信息提交后会在控制台会显示输入

# 03.Django学习之数据库
    # 控制台输入创建数据库：python3 manage.py makemigrations；python3 manage.py migrate。 db.sqlite3会生成test_database_userinfor的表
    # 示例一：提交数据后插入至数据库，前端展示所有的数据库信息
    url(r'^userInfor/', test_database_views.userInfor),  # 打开浏览器连接：http://127.0.0.1:8080/userInfor/，输入信息提交后会在控制台会显示输入,并且数据库会插入输入的数据

    # Django学习之视图函数
#     url(r"login", views.login),
#     url(r"yuan_back", views.yuan_back),

]





