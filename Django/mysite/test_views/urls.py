# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

from test_views import views

urlpatterns = [
    url(r'^home', views.home),
]