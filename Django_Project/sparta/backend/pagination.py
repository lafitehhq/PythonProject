#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.utils.safestring import mark_safe
from time import sleep
import commons


class PageInfo(object):

    def __init__(self, currentPage, totalItems, perItems=20, pageNum=11):
        self.__currentPage = commons.try_int(currentPage, 1)
        if self.__currentPage < 1:
            self.__currentPage = 1
        self.__perItems = perItems
        self.__totalItems = totalItems
        self.__pageNum = pageNum

    @property
    def current_page(self):
        return self.__currentPage

    @property
    def total_items(self):
        return self.__totalItems

    @property
    def total_page(self):
        if not self.__totalItems:
            self.__totalItems = 0
        val = self.__totalItems/self.__perItems +1 if self.__totalItems % self.__perItems >0 else self.__totalItems/self.__perItems
        return val

    @property
    def page_num(self):
        return self.__pageNum

    @property
    def start(self):
        val = (self.__currentPage - 1) * self.__perItems
        return val

    @property
    def end(self):
        val = self.__currentPage * self.__perItems
        return val

    def pager(self, url):
        '''
        page:当前页
        all_page_count: 总页数
        '''
        page_html = []
        page = self.current_page
        all_page_count = self.total_page
        total_items = self.total_items

        #首页
        '''
        first_html = u"<li><a href='%s?page=%s'>首页</a></li>" % (url,1)
        '''

        #上一页
        if page <= 1:
            first_html = u"<li class='disabled'><a href='javascript:void(0)'>首页</a></li>"
            prev_html = u"<li class='disabled'><a href='javascript:void(0)'>上一页</a></li>"
        else:
            first_html = u"<li><a href='%s?page=%s'>首页</a></li>" % (url,1)
            prev_html = u"<li><a href='%s?page=%s'>上一页</a></li>" % (url, page-1,)
        #page_html.append(first_html)
        page_html.append(prev_html)

        #11个页码
        if all_page_count < 11:
            begin = 0
            end = all_page_count

        #总页数大于 11
        else:
            #
            if page<6:
                begin = 0
                end = 11
            else:
                if page + 6 > all_page_count:
                    begin = page - 6
                    end = all_page_count
                else:
                    begin = page - 6
                    end = page + 5

        for i in range(begin,end):
            #当前页
            if page == i+1:
                a_html = u"<li class='active'><a href='%s?page=%s'>%d</a></li>" % (url, i+1, i+1, )
            else:
                a_html = u"<li><a href='%s?page=%s' >%d</a></li>" % (url, i+1, i+1, )
            page_html.append(a_html)
        #下一页
        if page+1>all_page_count:
            next_html = u"<li class='disabled'><a href='javascript:void(0)'>下一页</a></li>"
        else:
            next_html = u"<li><a href='%s?page=%s' >下一页</a></li>" % (url, all_page_count, )
        page_html.append(next_html)

        #尾页

        if page > 1 and page+1 > all_page_count:
            end_html = u"<li><a href='%s?page=%s' >尾页</a></li>" % (url, all_page_count, )
        else:
            end_html = u"<li><a href='javascript:void(0)'>尾页</a></li>"
        page_html.append(end_html)

        # 页码概要

        end_html = u"<li><a href='javascript:void(0)' >共 %d页 / %d 条数据</a></li>" % (all_page_count, total_items, )
        page_html.append(end_html)

        end_html = u"<li><a href='javascript:void(0)' >共 %d页</a></li>" % (all_page_count, )
        page_html.append(end_html)
        # 跳转至
        '''
        end_html = u"""<li><a class='pager-goto'><input class='inp' placeholder=' 跳转至' /></a><a href='javascript:void(0)' onclick='PageGo("%s?page=",this)' >GO</a></li>""" %(url)
        page_html.append(end_html)
        '''
        #将列表中的元素拼接成页码字符串
        page_string = mark_safe(''.join(page_html))

        return page_string

    def ajax_pager(self,baseurl):
        '''
        page:当前页
        all_page_count: 总页数
        '''
        page_html = []
        page = self.current_page
        all_page_count = self.total_page
        total_items = self.total_items

        #首页
        first_html = "<li><a href='javascript:void(0)' onclick='ChangePage(1)'>首页</a></li>"
        page_html.append(first_html)

        #上一页
        if page <= 1:
            prev_html = "<li class='disabled'><a href='javascript:void(0)'>上一页</a></li>"
        else:
            prev_html = "<li><a href='javascript:void(0)' onclick='ChangePage(%d)'>上一页</a></li>" % (page-1, )
        page_html.append(prev_html)

        #11个页码
        if all_page_count < 11:
            begin = 0
            end = all_page_count

        #总页数大于 11
        else:
            #
            if page<6:
                begin = 0
                end = 11
            else:
                if page + 6 > all_page_count:
                    begin = page - 6
                    end = all_page_count
                else:
                    begin = page - 6
                    end = page + 5

        for i in range(begin,end):
            #当前页
            if page == i+1:
                a_html = "<li class='active'><a href='javascript:void(0)' onclick='ChangePage(%d)'>%d</a></li>" % (i+1, i+1, )
            else:
                a_html = "<li><a href='javascript:void(0)' onclick='ChangePage(%d)'>%d</a></li>" % (i+1, i+1, )
            page_html.append(a_html)
        #下一页
        if page+1>all_page_count:
            next_html = "<li class='disabled'><a href='javascript:void(0)'>下一页</a></li>"
        else:
            next_html = "<li><a href='javascript:void(0)' onclick='ChangePage(%d)' >下一页</a></li>" % (all_page_count, )
        page_html.append(next_html)
        #尾页
        end_html = "<li><a href='javascript:void(0)' onclick='ChangePage(%d)' >尾页</a></li>" % (all_page_count, )
        page_html.append(end_html)

        # 页码概要
        end_html = "<li><a href='javascript:void(0)' >共 %d页 / %d 条数据</a></li>" % (all_page_count,total_items, )
        page_html.append(end_html)

        #将列表中的元素拼接成页码字符串
        page_string = mark_safe(''.join(page_html))

        return page_string