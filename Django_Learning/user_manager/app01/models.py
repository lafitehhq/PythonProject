from django.db import models

# Create your models here.

# 班级表
class Classes(models.Model):
    caption = models.CharField(max_length=32)  # 标题


# 学员表（一对多）
class Student(models.Model):
    name = models.CharField(max_length=32)  # 学员姓名
    cls = models.ForeignKey('Classes')  # ForignKey创建一对多关系；建立与Class的外键名为cls，默认与班级表的ID关联；注意：要加引号

    username = models.CharField(max_length=32)  # 学员的账号与密码
    password = models.CharField(max_length=32)


# 教师表（多对多）
class Teacher(models.Model):
    name = models.CharField(max_length=32)  # 教师姓名
    cls = models.ManyToManyField('Classes')  # ManytoMany创建多对多关系；会自动创建第三张表

    username = models.CharField(max_length=32)  # 教师的账号与密码
    password = models.CharField(max_length=32)

# 第三张

# 超管信息表
class Administrator(models.Model):
    username = models.CharField(max_length=32)  # 超管的账号与密码
    password = models.CharField(max_length=32)