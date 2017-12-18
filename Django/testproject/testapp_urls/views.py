# coding:utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.urls import reverse
from django.http import HttpResponseRedirect

# # 测试主页显示
# def index(request):
#     return HttpResponse(u'欢迎登录Django视图与网址测试')

# 测试自己编写的主页
def index(request):
    return render(request, 'home.html')

# GET方法进行网址跳转1.0
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

# GET方法进行网址跳转2.0
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

# # GET方法进行网址跳转3.0
# def old_add2_redirect(request, a, b):
#     return HttpResponseRedirect(
#         reverse('add2', args=(a, b))
#     )






