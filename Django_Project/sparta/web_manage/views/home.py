#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from web_manage.business import manager


def index(request):
    slider_list = manager.fetch_slider_list()
    course_list = manager.fetch_course_list()
    student_list = manager.fetch_student_list()
    student_detail = manager.fetch_student_detail()
    recruit_list = manager.fetch_recruit_list()
    cooperation_list = manager.fetch_cooperation_list()

    notice_list = manager.fetch_notice_list()

    return render(request, 'home/index.html', {'slider_list': slider_list,
                                               'course_list': course_list,
                                               'student_list': student_list,
                                               'student_detail': student_detail,
                                               'recruit_list': recruit_list,
                                               'cooperation_list': cooperation_list,
                                               'notice_list': notice_list})


def search(request, *arg, **kwargs):

    return render(request, 'home/search.html')


def detail(request, nid):

    return render(request, 'home/detail.html')


def about(request):
    return render(request, 'home/about.html')


def teacher(request):

    return render(request, 'home/teacher.html')


def students(request):
    detail_list = manager.fetch_all_student_detail()
    return render(request, 'home/students.html', {'detail_list': detail_list})


def problems(request):

    return render(request, 'home/problems.html')


def videos(request, *arg, **kwargs):
    # 获取分页信息
    current_page = request.GET.get('page', 1)

    # kwargs:方向ID，分类ID，难度ID
    response = manager.videos(current_page, request.path, **kwargs)

    return render(request, 'home/videos.html', {'model': response.data, 'current_url': response.current_url})
