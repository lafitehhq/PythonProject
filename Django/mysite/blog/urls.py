# -*- coding: utf-8 -*-

"""
# Django学习之urls：示例五：全局配置
"""

from django.conf.urls import url, include
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^news/stories/', views.introduce),
]