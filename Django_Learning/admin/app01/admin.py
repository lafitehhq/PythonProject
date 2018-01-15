from django.contrib import admin

# Register your models here.

from app01.models import *


class Myadmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "publication_date", "price")  # 按照表的字段显示表信息
    search_fields = ("title", "price")  # 按照表字段搜索,注意：字段名称是中文搜索时会报错
    list_filter = ("publisher_id", "title")  # 按照表字段建立过滤器
    ordering = ("-price",)  # 按照price的倒序(加负号)；正序（不加负号）
    fieldsets =[  # 格式：(** , {'fields': ['表字段名称']})   ；'classes': ['collapse']表示隐藏信息
        (None, {'fields': ['title']}),
        ('书籍信息', {'fields': ["publication_date", 'price', "publisher", ], 'classes': ['collapse']}),
    ]




# 表名称要与models.py中的对应的类名称一致
admin.site.register(Book, Myadmin)  # 加载表且按照自定义的样式显示
admin.site.register(Publisher)
admin.site.register(Author)