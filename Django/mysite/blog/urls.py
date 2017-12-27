# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^new/stories', views.introduce),
]