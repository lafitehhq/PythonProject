"""
模板语言--变量（使用双大括号来引用变量）；标签(tag)的使用；自定义filter和simple_tag
浏览器打开http://127.0.0.1:8000/index/，前端页面会输出指定的后端传值类型
"""

from django.shortcuts import render, HttpResponse

# Create your views here.

import datetime


def index(req):
    s1 = 'hello'
    # return render(req, "index.html", {"obj_str": s1})

    # 打印列表中某个元素
    s2 = [1, 22, 333]
    # return render(req, "index.html", {"obj_list": s2})

    # 打印字典中某个元素
    s3 = {"username": "Vito", "age": "25"}
    # return render(req, "index.html", {"obj_dir": s3})

    # 打印函数的返回值
    s4 = datetime.datetime.now()
    # return render(req, "index.html", {"obj_fun": s4})

    # 打印自定义类的传参值
    # class Person:
    #     def __init__(self, name, age):
    #         self.name = name
    #         self.age = age

    # s5 = Person("Yanina", 22)
    # return render(req, "index.html", {"obj_class": s5})

    s6 = "<a href = 'http://www.vitowong.top'>跳转至我的博客</a>"
    return render(req, "index.html", {"obj_code": s6})


def login(req):
    if req.method == "POST":
        return HttpResponse("ok")

    return render(req, "login.html")


def index2(req):
    number2 = 30
    return render(req, "index2.html", {"num2":number2})

def index3(req):
    number3 = 50
    return render(req, "index3.html", {"num3": number3})


def ordered(req):
    return render(req, "ordered.html")

def shopping_car(req):
    return render(req, "shopping_car.html")

def ordered_1(req):
    return render(req, "ordered_1.html")

def shopping_car_1(req):
    return render(req, "shopping_car_1.html")


