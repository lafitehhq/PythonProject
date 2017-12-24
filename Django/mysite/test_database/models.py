from django.db import models

# Create your models here.

# 提交表单提交的数据至数据库并展示
# 创建一个UserInfor表
class UserInfor(models.Model):
    username = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
