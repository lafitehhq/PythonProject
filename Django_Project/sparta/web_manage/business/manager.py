#!/usr/bin/env python
# -*- coding:utf-8 -*-

from web_models import models
from backend.response import BaseResponse
from backend.pagination import PageInfo


def fetch_slider_list():
    """ 获取首页轮播图片（在线状态）
    :return: 返回轮播列表
    """
    slider_list = models.BxSlider.objects.filter(status=1).values('img', 'href')

    return slider_list


def fetch_course_list():
    """ 获取课程列表
    :return: 返回轮播列表
    """
    course_list = models.Course.objects.filter(status=1).order_by('-weight').values('id', 'icon', 'name', 'summary')

    return course_list

def fetch_student_list():
    """ 获取就业学生列表
    :return:
    """
    course_list = models.Student.objects.filter(status=1).order_by('-weight').values('id', 'pic', 'name', 'company', 'salary')[0:5]

    return course_list


def fetch_student_detail():
    """ 获取第一个学员详细信息
    :return:
    """
    student_detail = models.StudentDetail.objects.all().order_by('-weight').values('letter_of_thanks', 'student__pic', 'student__name', 'student__company', 'student__salary').first()

    return student_detail


def fetch_all_student_detail():
    """ 获取所有学员详细信息"""

    student_detail = models.StudentDetail.objects.all().order_by('-weight').values('letter_of_thanks', 'student__pic', 'student__name', 'student__company', 'student__salary')

    return student_detail

def fetch_recruit_list():
    """ 获取招聘信息
    :return:
    """
    recruit_list = models.Recruit.objects.all().order_by('-weight').values('id', 'title', 'salary')[0:10]

    return recruit_list


def fetch_cooperation_list():
    """ 获取企业合作
    :return:
    """
    recruit_list = models.Cooperation.objects.all().order_by('-weight').values('id', 'href', 'logo', 'company')

    return recruit_list


def fetch_notice_list():
    """ 获取最新公告
    :return:
    """
    recruit_list = models.Notice.objects.filter(status=1).order_by('-weight').values('id', 'title', 'content')[0:3]

    return recruit_list


def try_int(arg, default=0):
    try:
        arg = int(arg)
    except Exception, e:
        arg = default
    return arg


def convert_value_int(kwargs):
    for key, value in kwargs.items():
        val = try_int(value)
        if not val:
            del kwargs[key]
        else:
            kwargs[key] = val


def videos(current_page, current_url, **kwargs):
    response = BaseResponse()
    try:
        ret = {}
        # 将kwargs:方向ID，分类ID，难度ID转换成数字
        convert_value_int(kwargs)
        #
        direction_id = kwargs.pop('direction_id', None)

        # 获取所有的方向
        ret['direction'] = models.Direction.objects.all().values('id', 'name')
        # 获取所有的级别
        ret['level'] = map(lambda x: {'id': x[0], 'name': x[1]}, models.Video.level_choice)

        # 如果指定分类
        if kwargs.get('classification__id', None):
            # 如果指定了方向
            if direction_id:
                # 获取当前方向的所有分类
                classification_obj_list = models.Direction.objects.get(id=direction_id).classification.all()
                classification_list = map(lambda x: x[0], classification_obj_list.values_list('id'))

                # 如果当前分类 在分类中...
                if kwargs.get('classification__id') in classification_list:
                    pass
                else:
                    # 如果当前分类不在选中方向中，则选中全部
                    # show c all
                    del kwargs['classification__id']
                    # modify url
                    url_elements = current_url.split('-')
                    url_elements[2] = '0'
                    current_url = '-'.join(url_elements)
                    print current_url
                # 构造分类关键字，用于获取视频的条件
                kwargs['classification__id__in'] = classification_list
                # 获取方向下的所有分类，用于页面展示
                ret['classification'] = classification_obj_list.values('id', 'name')
            # 未指定方向
            else:
                # 直接获取所有的分类，用于页面显示
                ret['classification'] = models.Classification.objects.all().values('id', 'name')
        # 如果未指定分类
        else:

            if direction_id:
                classification_obj_list = models.Direction.objects.get(id=direction_id).classification.all()
                classification_list = map(lambda x: x[0], classification_obj_list.values_list('id'))
                kwargs['classification__id__in'] = classification_list
                ret['classification'] = classification_obj_list.values('id', 'name')
            else:
                # get all and show all c
                ret['classification'] = models.Classification.objects.all().values('id', 'name')

        kwargs['status'] = 1
        total_item = models.Video.objects.filter(**kwargs).count()

        page_info = PageInfo(current_page, total_item)
        ret['result'] = models.Video.objects.filter(**kwargs).order_by('-weight')[page_info.start:page_info.end]
        ret['total_item'] = total_item
        ret['pager'] = page_info.pager(current_url)

        response.current_url = current_url
        response.status = True
        response.data = ret

    except Exception, e:
        print e
        response.message = str(e)

    return response



