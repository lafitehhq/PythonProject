from django.db import models

# Create your models here.

# 示例二：提交数据并展示(数据库)
class UserInfor(models.Model):

    username=models.CharField(max_length=64)
    sex=models.CharField(max_length=64)
    email=models.CharField(max_length=64)
