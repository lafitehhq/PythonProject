#!/usr/bin/python
# coding:utf-8

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __unicode__(self):
        return self.title
