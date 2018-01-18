开发流程:
①：在\app01\models.py中定义所有的表结构
②：python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
    ||
③：在\templates\**.html中编写静态登录页面
    ||
④：在\user_manager\urls.py中配置url跳转信息
    ||
⑤：在\app01\views.py中定义**函数


login.html  --> index.html --> views.py