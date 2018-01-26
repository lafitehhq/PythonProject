#!/usr/bin/env python
#coding:utf-8

from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag
def generate_classification_url(nid, current_url, n, text, all_direction):
    str_list = current_url.split('-')
    if n == 3:
        selected_id = str_list[3].split('.')[0]
    else:
        selected_id = str_list[n]

    if n == 3:
        str_list[3] = str(nid) + '.html'
    else:
        str_list[n] = str(nid)

    if not all_direction:
        str_list[2] = '0'

    if int(selected_id) == nid:
        result = "<a class='selected' href='javascript:void(0);'>%s</a>" % (text,)
    else:
        result = "<a href='%s'>%s</a>" % ('-'.join(str_list), text)

    return result


@register.simple_tag
def generate_url(nid, current_url, n, text):

    str_list = current_url.split('-')

    if n == 3:
        selected_id = str_list[3].split('.')[0]
    else:
        selected_id = str_list[n]

    if n == 3:
        str_list[3] = str(nid) + '.html'
    else:
        str_list[n] = str(nid)

    if int(selected_id) == nid:
        result = "<a class='selected' href='javascript:void(0);'>%s</a>" % (text,)
    else:
        result = "<a href='%s'>%s</a>" % ('-'.join(str_list), text)

    return result


@register.filter
def random_flow(value, args):
    print(value,args)
    divisor, remainder = args.split(',')
    divisor = int(divisor)
    remainder = int(remainder)
    if value % divisor == remainder:
        return True
    return False