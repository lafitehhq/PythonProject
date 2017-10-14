import pymysql

# 步骤1：创建数据库连接：让python连接上数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='sqlexample', chartset='utf8')
# 步骤2：创建游标：让python操作数据库
cursor = conn.cursor()

# 步骤3：执行SQL语句
## 向caption插入数据
cursor.execute('insert into class(caption) values("Vito")')
## 返回受影响行数
effect_row = cursor.execute("updata hosts set host = '1.1.1.2'")

# 步骤4：提交
conn.commit()
# 步骤5：关闭游标
cursor.close()
# 步骤6：关闭数据库
conn.close()

