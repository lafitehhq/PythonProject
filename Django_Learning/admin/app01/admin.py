from django.contrib import admin

# Register your models here.

from app01.models import *


class Myadmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "publication_date", "price")  # 按照表的字段显示表信息



# 表名称要与models.py中的对应的类名称一致
admin.site.register(Book, Myadmin)  # 加载表且按照自定义的样式显示
admin.site.register(Publisher)
admin.site.register(Author)