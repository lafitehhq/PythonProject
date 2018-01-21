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
1.Cookie
    1.1.含义
        保存在浏览器端的键值对；可以利用做登录
    1.2.特点
        1、保存在用户浏览器
        2、可以主动清除
        3、也可以被“伪造”
        4、跨域名cookie不共享
        5、浏览器设置不接受cookie
        6、客户端与服务器传输数据包含两个方面：头部+内容。cookie是包含在请求头或响应头中的
    1.3.属性
        max_age:设置cookie的失效时间
    1.4.设置
        1.4.1.服务端操作cookie
            1.4.1.1
                obj.set_cookie('k1','v1')
                obj.set_cookie('k1','v1',max_age=10)
            1.4.1.2
                v = datetime.datetime.utcnow() + datetime.timedelta(seconds=10)
                obj.set_cookie('k1','v1',max_age=10,expires=v)
            1.4.1.3.path:
                /       表示，全局生效
                /xxxx/  表示，只有当前url生效
            1.4.1.4.domian:
                obj.set_cookie('k4','v4',max_age=10,expires=v, domain='oldboy.com')
                obj.set_cookie('k1','v1')
            1.4.1.5.httponly: 仅仅HTTP网络传输使用

        1.4.2.客户端操作cookie
            1.4.2.1.方式1:使用dom          --> 麻烦
            1.4.2.2.方式2:使用jquery插件   -->
                                            jquery.cookie.js
                                            jquery-2.1.4.min.js
                                        示例：（在浏览器端的console中编写）
                                        d = new Date()  # 获得当前时区的时间
                                        d.getDate()  # 获取当前时区的日期
                                        d.setDate()  # 设置当前时区的日期
                                        d.setDate(d.getDate()+7)  # cookie7天后失效

     1.5.应用：
        1.5.1.登录认证的2种cookie:
            普通cookie---不推荐
                - 敏感信息（直接看到），不宜放置在cookie中，敏感信息放在数据库，频繁操作数据库
            签名(加密)的cookie---不推荐
                - 敏感信息（可能会解密）
            敏感信息不宜放置在cookie中，放在数据库，频繁操作数据库

2.Session：
    2.1.含义
        session是服务器端的一个键值对
        session内部机制依赖于cookie
    2.2.
        request.session['k']
        request.session['k1'] = v
        request.session['k2'] = v

        del request.session['k1']
        request.session.clear()


    # 获取、设置、删除Session中数据
    request.session['k1']
    request.session.get('k1',None)



    request.session['k1'] = 123
    request.session.setdefault('k1',123) # 存在则不设置
    del request.session['k1']

    # 所有 键、值、键值对
    request.session.keys()
    request.session.values()
    request.session.items()
    request.session.iterkeys()
    request.session.itervalues()
    request.session.iteritems()


    # 用户session的随机字符串
    request.session.session_key

    # 将所有Session失效日期小于当前日期的数据删除
    request.session.clear_expired()

    # 检查 用户session的随机字符串 在数据库中是否
    request.session.exists("session_key")

    # 删除当前用户的所有Session数据
    request.session.delete("session_key")


