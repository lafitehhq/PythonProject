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

   2.4.写CRM视图
       创建销售的视图：复制\PerfectCRM\urls.py至\PerfectCRM\crm的App中编写销售的方法 ==>
           在主项目中的urls中配置  url(r'^crm/', include("crm.urls"))  表示引用crm中的urls
           在APP中的urls中配置     url(r'^$', views.index, name="sales_index") 表示销售App中的主页面

   2.5.用户登录账户显示
           在index.html中的




