import pymysql

# 步骤1：创建数据库连接：让python连接上数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='sqlexample', chartset='utf8')
# 步骤2：创建游标：让python操作数据库
cursor = conn.cursor()

# 步骤3：执行SQL语句
## 3.1：增
## 3.1.1：单条单个数据
# inp = input('请输入班级：')
# r1 = cursor.execute('insert into class(caption) values(%s)', inp)
# print(r1)  # 返回受影响的行数
## 3.1.2：单条多个数据
# inp = input('请输入学生信息')
# r1 = cursor.execute('insert into student(gender, class_id, sname) values(%s , %s, %s)', ('女', '4', '刘悦'))
## 3.1.3：多条多个数据
l = (
    ('女', '4', '林启玲'),
    ('女', '4', '梁梓灵'),
    ('女', '4', '高莹'),
    ('女', '4', '黄涛'),
)
r1 = cursor.executemany('insert into student(gender, class_id, sname) values(%s , %s, %s)', l)
## 3.2：删
r2 = cursor.execute('delete from score where sid = %', (54, ))
## 3.3：改
r3 = cursor.execute('update student set gender = %s where sid = %d', ('男', 4))
## 3.4：查(注意：不要commit，即不用写步骤4)
r4 = cursor.execute('select * from student')
print(r4)
## 3.4.1：查询所有数据
result1 = cursor.fetchall()
print(result1)
## 3.4.2：查询第一条数据
result2 = cursor.fetchone()
print(result2)
## 3.4.1：查询指定条数数据
result3 = cursor.fetchmany(3)
print(result3)



effect_row = cursor.execute("updata hosts set host = '1.1.1.2'")

# 步骤4：提交
conn.commit()
# 步骤5：关闭游标
cursor.close()
# 步骤6：关闭数据库
conn.close()

