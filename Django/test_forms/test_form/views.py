from django.shortcuts import render

# Create your views here.

# 示例一：在前台用 get 或 post 方法提交一些数据
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

# 示例二：
