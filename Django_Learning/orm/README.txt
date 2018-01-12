 对象关系映射
----------------------------------------------------------------------------
 书籍模型：书籍有书名和出版日期，一本书可能会有多个作者，一个作者也可以写多本书，
 出版商和书籍是一对多关联关系[ 一本书只应该由一个出版商出版](one－to－many),也被称作外键
 作者和书籍的关系就是多对多的关联关系（many－to－many），
----------------------------------------------------------------------------
1.主键特点：非空且唯一
2.save与update的区别：
①：update比save性能更优，save会将所有的数据更新一遍，update只会修改要改的字段
----------------------------------------------------------------------------

----------------------------------------------------------------------------
 1.创建表
    1.2.单表
    1.3.关联表
        1.3.1.一对一 (OnetoOne)
            通过两个Foreignkey和unique=true

        1.3.2.一对多 (ForeignKey)
            1.3.2.1.特点
            在哪个表要创建该表的就是"多"，关键字括住的就是"一"；
            1.3.2.2.例子
            publisher = models.ForeignKey("Publisher")  # 在书籍表建立一个关于出版社表的外键，表示一个出版社可以出多本书

        1.3.3.多对多 (ManyToMay)
            1.3.3.1.特点
            通过两个Foreignkey



 2.操作表 (行对象操作)
    2.1.增
        2.1.1.create(声明对象)
            2.1.1.1:单表没有外键
                2.1.1.1.1:方式1
                models.Book.objects.create(title="Python",price=12)
                2.1.1.1.2:方式2
                dic={"title":"Go","price":45}
                models.Book.objects.create(**dic)
            2.1.1.2:有外键
            一对多:
                2.1.1.2.1:方式1
                models.Book.objects.create(title="Python",price=12,publish_id=2)
                2.1.1.2.2:方式2(推荐)
                models.Book.objects.create(title="Python",price=12,publish=obj)
             多对多:
                2.1.1.3.1:正向查询+添加
                book=models.Book.objects.filter(id=2)[0]
                authors=models.Author.objects.filter(id__gt=2)
                book.author.add(*authors)  # 为书籍绑定作者
                2.1.1.3.2:反向查询+添加
                author=models.Author.objects.filter(id=3)[0]
                books=models.Book.objects.filter(id__gt=2)
                author.book_set.add(*book) # 生加一个_set;为作者绑定书籍
                2.1.1.3.3:自己创建第三张表
                models.Book2Author.objects.create(
                    book_id=2,
                    author_id=3
                )

        2.1.2.save
            2.1.2.1:方式1--实例化对象+保存至数据库
                obj=Book(title="Python",price=12)
                obj.save()
            2.1.2.2:方式2--实例化对象+保存至数据库
                obj=Book()
                obj.title="Go"
                obj.price=45
                obj.save()



    2.2.删
    2.3.改
    2.4.查

3.惰性机制
    3.1.在settings添加Loging配置日志记录部分
    LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}