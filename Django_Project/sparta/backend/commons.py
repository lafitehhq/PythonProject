#!/usr/bin/env python
# -*- coding:utf-8 -*-


def try_int(arg, default=0):
    try:
        arg = int(arg)
    except Exception, e:
        arg = default
    return arg
