# -*- coding:utf-8 -*-
"""
自定标签的写法:
①：引入两个头文件
②：实例化一个装饰器register
③：@register.simple_tag
"""
from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register是固定的变量名，不能改变

@register.simple_tag
def my_add100(v1):
    return v1 + 100

@register.simple_tag
def my_add(v1, v2, v3):
    return v1 + v2 + v3