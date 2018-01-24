"""user_manager URL Configuration

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

from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
# ##############测试cookies方式登录1.0##############
    # url(r'^login.html$', views.login),
    # url(r'^index.html$', views.index),
    # url(r'^js_cookie.html', views.js_cookie),

# ##############测试session方式登录与注销##############
    # url(r'^login_2.html$', views.login_2),
    # url(r'^index_2.html$', views.index_2),
    # url(r'^logout_2.html$', views.logout_2),  # 注意：不用额外写logout_2.html,只要在index_2,urls.py中添加logout_2函数

# ##############测试swssion + 迭代器方式登录与注销##############
    # url(r'^login_3.html$', views.login_3),
    # url(r'^index_3.html$', views.index_3),
    # url(r'^logout_3.html$', views.logout_3),
    # url(r'^classes.html$', views.handle_classes),
    # url(r'^teacher.html$', views.handle_teacher),
    # url(r'^student.html$', views.handle_student),

    url(r'^login_3.html$', views.Login.as_view()),
    # url(r'^index_3.html$', views.index_3),
    # url(r'^logout_3.html$', views.logout_3),
    # url(r'^classes.html$', views.handle_classes),
    # url(r'^teacher.html$', views.handle_teacher),
    # url(r'^student.html$', views.handle_student),


]
