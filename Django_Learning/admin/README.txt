1.admin常用命令
python3 manage.py makemigration
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver


2.页面展示常用设置
    2.1.整个系统汉化
        在settings.py中将 # LANGUAGE_CODE = 'en-us'  修改成 LANGUAGE_CODE = 'zh-hans'
    2.2.按照表的字段显示表信息
        list_display = ()
    2.3.按照表字段搜索
        search_fields = ()
    2.4.按照表字段建立过滤器
        list_filter = ()
    2.5.按照表字段升降序排列
        ordering = ()
    2.6.按照自定义要显示的信息表示
        # 格式：(** , {'fields': ['表字段名称']})   ；'classes': ['collapse']表示隐藏信息
        fieldsets =[
            (),()
            ]

3.链接mysql数据库
    3.1.启动并创建库
        mysql -hlocalhost -uroot -p 和 create database ORM; 和 show databases;
    3.2.配置setting.py
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "ORM",  # 连接名称为ORM的数据库
            "HOST": "localhost",
            "PORT": "3306",
            "USERNAME": "root",
            "PASSWORD": "123456",
        }
    }

