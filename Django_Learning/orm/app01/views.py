from django.shortcuts import render, HttpResponse

# Create your views here.

"""
Django的惰性机制
"""
from app01.models import Book
from app01 import models
from django.db.models import Avg,Min,Sum,Max

def data_oper(req):

# 1.Django的惰性机制
    obj_set = models.Book.object.filter(id=2)  # 获得querySet对象，此句并不走数据库
    # 1.1:验证Django的缓存机制
#     for obj in obj_set:
#         print(obj.title)
#     obj_set.update(title="yyy")  # 不加此句只有两个for循环不走数据库只走缓存，加上此句既走数据库也走缓存
#     for obj in obj_set:
#         print(obj.title)
    # 1.2:使用迭代器解决所有数据放进缓存池的问题
#     if obj_set.iterator():
#         pass
    # 1.3:对querySet对象进行切片,走了数据库
#     obj = obj_set[0]

# ###################################################################################################################################

# 2.对象形式的查找
    # 2.1.正向查找
    obj1 = models.Book.objects.filter(title="Go")[0]  # 查询某本书的出版社所在的城市
    print(obj1.publisher.city)
    ret1 = models.Book.objects.first()
    print(ret1.title)
    print(ret1.price)
    print(ret1.publisher)
    print(ret1.publisher.name)  # 因为一对多的关系所以ret1.publisher是一个对象,而不是一个queryset集合
    # 2.2.反向查找
    obj2 = models.Publish.objects.filter(name="人民出版社")  # 查询出版社是"人民出版社"的数据
    print(obj2.book_set.all.values("title").distinct())  # distinct(),对结果去重
    ret2 = models.Publish.objects.last()
    print(ret2.name)
    print(ret2.city)
    # 如何拿到与它绑定的Book对象呢?
    print(ret2.book_set.all())  # ret2.book_set是一个queryset集合

# ###################################################################################################################################

# 3.双下划线(__)之单表条件查询
    models.Book.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
    models.Book.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
    models.Book.objects.exclude(id__in=[11, 22, 33])  # not in
    models.Book.objects.filter(name__contains="ven")  # 区分大小写过滤的
    models.Book.objects.filter(name__icontains="ven")  # 不区分大小写过滤的
    models.Book.objects.filter(id__range=[1, 2])   # 范围bettwen and
    models.Book.objects.filter(title__startwith="P")  # startswith，istartswith, endswith, iendswith,

# ###################################################################################################################################

# 4.双下划线(__)之多表条件关联查询
    # 4.1.正向查找(条件)
    ret3 = models.Book.objects.filter(title='Python').values('id')
    print(ret3)#[{'id': 1}]
    # 4.1.1.正向查找(条件)之一对多
    ret4 = models.Book.objects.filter(title='Python').values('publisher__city')
    print(ret4)  #[{'publisher__city': '北京'}]
    # 4.1.2.正向查找(条件)之多对多
    ret5 = models.Book.objects.filter(title='Python').values('author__name')
    print(ret5)
    ret6 = models.Book.objects.filter(author__name="alex").values('title')
    print(ret6)
    # 注意
    # 正向查找的publisher__city或者author__name中的publisher,author是book表中绑定的字段
    # 一对多和多对多在这里用法没区别

# 4.2.反向查找(条件)
    # 4.2.1.反向查找之一对多:
    ret8 = models.Publisher.objects.filter(book__title='Python').values('name')
    print(ret8)#[{'name': '人大出版社'}]  注意,book__title中的book就是Publisher的关联表名
    ret9 = models.Publisher.objects.filter(book__title='Python').values('book__authors')
    print(ret9)#[{'book__authors': 1}, {'book__authors': 2}]
    # 4.2.2.反向查找之多对多:
    ret10 = models.Author.objects.filter(book__title='Python').values('name')
    print(ret10)#[{'name': 'alex'}, {'name': 'alvin'}]
    # 注意
    # 正向查找的book__title中的book是表名Book
    # 一对多和多对多在这里用法没区别

# ###################################################################################################################################

# 5.聚合查询和分组查询
# 5.1.聚合查询--aggregate(*args,**kwargs):通过对QuerySet进行计算，返回一个聚合值的字典。aggregate()中每一个参数都指定一个包含在字典中的返回值。即在查询集上生成聚合
    # 计算所有在售书的平均价钱。
    Book.objects.all().aggregate(Avg('price'))# {'price__avg': 34.35}
    Book.objects.aggregate(average_price=Avg('price'))  # {'average_price': 34.35}
    # 所有图书价格的最大值和最小值：
    Book.objects.aggregate(Avg('price'), Max('price'), Min('price')) # {'price__avg': 34.35, 'price__max': Decimal('81.20'), 'price__min': Decimal('12.99')}
    # 查询alex出的书总价格
    Book.objects.filter(author__name='alex').aggregate(Sum('price'))
# 5.2.分组查询--annotate(*args,**kwargs):可以通过计算查询结果中每一个对象所关联的对象集合，从而得出总计值(也可以是平均值或总和)，即为查询集的每一项生成聚合
    # 查询各个作者出的书的总价格,这里就涉及到分组了，分组条件是authors__name
    Book.objects.values("author__name").annotate(Sum('price'))
    # 查询各个出版社最便宜的书价是多少
    Book.objects.values("publisher__name").annotate(Min('price'))

    return HttpResponse("前端打印ok")

        


