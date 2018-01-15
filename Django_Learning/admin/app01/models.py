from django.db import models

# Create your models here.

from django.db import models

# 出版社表
class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name="名称")
    address = models.CharField("地址", max_length=50)
    city = models.CharField('城市', max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 作者表
class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# 作者信息表
class AuthorDetail(models.Model):
    sex = models.BooleanField(max_length=1, choices=((0, '男'), (1, '女'),))
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author)

# 书籍表
class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10)
    publication_date = models.DateField()
    publisher = models.ForeignKey("Publisher")  # 一对多的关系；在书籍表建立一个关于出版社表的外键，表示一个出版社可以出多本书
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

class Book2Author(models.Model):
    # 建立多对多关系
    author = models.ForeignKey("Author")
    book = models.ForeignKey("Book")
    # 建立联合唯一关系（非必须的）
    class Meta:
        unique_together=["author", "book"]
