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
from django.conf.urls import url, include
from django.contrib import admin

# from testapp_urls import views as testapp_urls_views
from testapp_templates import views as testapp_templates_views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),  # 测试默认的主页显示

    # # 测试testapp_url的配置
    # url('add/', testapp_urls_views.add, name='add'),  # 测试网址跳转1.0:a=4&b=5 ;访问连接：http://127.0.0.1:8000/add/?a=4&b=5
    # url(r'^add/(\d+)/(\d+)/$', testapp_urls_views.add2, name='add2'),  # 测试网址跳转2.0:/add/4/5/ ;访问连接：http://127.0.0.1:8000/add/4/5/
    # url(r'^$', testapp_urls_views.index),  # 测试自己编写的主页显示
    # # 测试网址跳转3.0

    # 测试testapp_templates的配置
    url(r'^$', testapp_templates_views.home, name='home'),

]


