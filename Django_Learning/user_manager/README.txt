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
        cookie发送到服务器端依附于请求头中，返回客户端依附于响应头中
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
        session内部机制依赖于cookie去实现
    2.2.session的常见操作
        2.2.1.获取、设置、删除Session中数据
            request.session['k1']
            request.session.get('k1',None)

            request.session['k1'] = 123
            request.session.setdefault('k1',123) # 存在则不设置

            del request.session['k1'] # 删除某个swssion
            request.session.clear()  # 删除所有的session

        2.2.2.所有 键、值、键值对
            request.session.keys()
            request.session.values()
            request.session.items()
            request.session.iterkeys()
            request.session.itervalues()
            request.session.iteritems()

        2.2.3.用户session的随机字符串session_key
            request.session.session_key

        2.2.4.将所有Session失效日期小于当前日期的数据删除,默认超时时间是14天
            request.session.clear_expired()

        2.2.5.检查用户session的随机字符串 在数据库中是否
            request.session.exists("session_key")

        2.2.6.删除当前用户的所有Session数据
            request.session.delete("session_key")

    2.3.session在setting.py中的设定配置
            SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 引擎（默认）
            SESSION_COOKIE_NAME = "sessionid"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
            SESSION_COOKIE_PATH = "/"  # Session的cookie保存的路径（默认）
            SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名（默认）
            SESSION_COOKIE_SECURE = False  # 是否Https传输cookie（默认）
            SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输（默认）
            SESSION_COOKIE_AGE = 1209600  # Session的cookie失效日期（2周）（默认）
            SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期（默认）
            SESSION_SAVE_EVERY_REQUEST = False  # 是否每次请求都保存Session，默认修改之后才保存（默认）

     2.4.session比cookie的优点
        cookie无论是普通写法还是加密写法，所有信息都存在于客户端；session只存放session id(随机字符串)于客户端，敏感信息都存放于服务器端

     2.5.session的工作原理
        客户器向服务器端发请求消息
                ||
        服务器端检查该客户端发来的请求里是否包含了一个SESSION ID
                ||
        ①：若客户端请求包含了一个SESSION ID，则说明该用户已登陆过且服务器端为该客户端创建过SESSION --> 服务器端按照这个SESSION ID把这个SESSION在服务器的内存中查找出来，如果查找不到，就新创建一个。
        ②：若客户端请求里不包含SESSION ID，服务器端则为该客户端创建一个SESSION并生成一个与此相关的SESSION ID。
                ||
        SESSION ID(唯一的、不重复的、不容易找到规律的字符串)将被在本次响应中返回到客户端保存,保存这个SESSION ID的正是COOKIE
                ||
        再次访问时，SESSION ID(作为key)在服务器中找SESSION(作为value)






