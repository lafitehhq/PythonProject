0.登录信息：
root
lafitehhq@126.COM
qead..8900882


1. 需求分析：
   见CRM功能图.png

2. 步骤：
   2.0.在本机中创建数据库：create database PerfectCRM charset utf8；
   2.1.crm\models.py创建表 ==> PerfectCRM\settings.py配置MySQL驱动；__init__.py配置MySQL库驱动 ==> 创建超管用户
   2.2.创建statics目录存放静态文件
           创建statics目录，注意：名称一定要是statics，前端是通过默认的    STATIC_URL = '/static/' 中的static别名去寻找静态文件
           在\PerfectCRM\settings.py中引入静态文件目录
               STATICFILES_DIRS = (
                    os.path.join(BASE_DIR, "statics"),
                    )
           在静态目录\PerfectCRM\statics中创建4个子目录:js，css，fonts(字体)，plugins(插件)
           将下载模板的css，js文件放入对应的目录中
   2.3.创建\templates\base.html用于存放css，js模板 ==> \templates\index.html用于存放下载的Bootstrapt模板。
           在base.html中使用标签作为模板：
                {% block body %} {% endblock %}
           在index.html中使用标签引用静态文件：
                {% extends 'base.html' %} 且用{% block body %} {% endblock %}包裹<body></body>
                将index.html中js和css引用文件注释挪到base.html中
           在base.html中配置静态文件的路径：
                <link rel="icon" href="/static/imgs/Yanina.ico">  <!--网页标签栏图标-->
                <title>Vito's CRM</title> <!--网页标签栏信息-->
                css，js，bootstrapt中的路径都改成/static/**中
           在index.html中精简显示元素：

   2.4.写销售(CRM)视图
       创建销售的视图：复制\PerfectCRM\urls.py至\PerfectCRM\crm的App中编写销售的方法 ==>
           在主项目中的urls中配置  url(r'^crm/', include("crm.urls"))  表示引用crm中的urls
           在APP中的urls中配置     url(r'^$', views.index, name="sales_index") 表示销售App中的主页面

   2.5.用户登录账户显示
       2.5.1.在\PerfectCRM\crm\models.py中创建菜单表(class Menu),并在角色表(class Role)zhong 建立多对多关系 ==> 在PerfectCRM\crm\admin.py中配置 admin.site.register(models.Menu) ==> makemigrations生成表
       2.5.2.新建在\PerfectCRM\templates中创建不同角色的文件夹：king_admin，sales，student
       2.5.3.新建销售首页(sales_index)，学生首页(stu_index)，客户库(customer_list)首页
       2.5.3.1客户库(customer_list)首页
            在\PerfectCRM\crm\urls.py中配置 url(r'^customers/$', views.customer_list, name="customer_list")【注意：前端页面关联的别名用customer_list】,  ==> 在\PerfectCRM\crm\views.py 中编写 def customer_list(request)  ==>在\PerfectCRM\templates\sales中新建customers.html ==> 继承index.html【而非静态的base.html文件】 ==> 在\PerfectCRM\templates\index.html中将可变的内容用{% block page-content %}与{% endblock %}框住可变代码  ==> 在customers.html中使用{% block page-content %}与{% endblock %} ==> 登录http://127.0.0.1:8000/crm/customers/查看销售首页显示正常 ==> 在后台中的角色表中添加

       2.5.4. 添加角色所能看的表
           在后台中的角色表中创建角色--选择角色对应可看的表
       2.5.5. 用户与角色关联
           在后台中的用户表中为用户添加角色
       2.5.6. 角色动态菜单显示
           在\PerfectCRM\templates\index.html中的<ul></ul>使用标签获取数据库中内容

    2.6.编写动态admin模板app--king_admin
       2.6.1.创建king_admin的app，在\PerfectCRM\PerfectCRM\settings.py中配置king_app
       2.6.2.在\PerfectCRM\PerfectCRM\urls.py中配置引入king_admin的App中的urls： url(r'^king_admin/', include("king_admin.urls")),


       2.6. 创建自定义标签
            创建templatetags目录，创建tags.py  ==> 在\PerfectCRM\templates\king_admin\table_index.html中引入自定义标签 {% load tags %} ==> 在







