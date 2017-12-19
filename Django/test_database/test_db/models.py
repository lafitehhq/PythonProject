from django.db import models

# Create your models here.

# 新建了一个Person类，继承自models.Model, 一个人有姓名和年龄。
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return (self.name)
