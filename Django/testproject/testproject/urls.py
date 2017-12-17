"""testproject URL Configuration

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

from testapp_urls import views as testapp_urls_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', testapp_urls_views.index),  # 测试主页的显示
    url('add/', testapp_urls_views.add, name='add'),  # 测试/add/3/4/ 这样的网址的方式跳转,访问连接：http://127.0.0.1:9999/add/?a=4&b=5
    url(r'^add2/(\d+)/(\d+)/$', testapp_urls_views.add2, name='add2'),  # 测试有 /add/4/5/ ，访问时就会自动跳转到新的/new_add/4/5
]


