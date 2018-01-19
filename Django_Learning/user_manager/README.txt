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






------------------------------------------------------------------------------------------------
知识点：
Cookie：保存在浏览器端的键值对；可以利用做登录
    1、保存在用户浏览器
    2、可以主动清除
    3、也可以被“伪造”
    4、跨域名cookie不共享
    5、浏览器设置不接受cookie