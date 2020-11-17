# coding: utf-8

import mysql.connector

# 创建数据库连接
db = mysql.connector.connect(
    host='192.168.28.48',
    user='root',
    passwd='123456'
)

my_cursor = db.cursor()

# 创建数据库
#my_cursor.execute("CREATE DATABASE test")

# 查看数据库是否存在
#my_cursor.execute("SHOW DATABASES")

#for i in my_cursor:
#    print(i)

# 创建数据库表
my_cursor.execute("use test;")
#my_cursor.execute("CREATE TABLE sites(name varchar(255), url varchar(255))")

# 设置主键
#my_cursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#my_cursor.execute("SHOW TABLES")
#for t in my_cursor:
#    print(t)

#my_cursor.execute("desc sites;")

# 插入一条数据
sql = "INSERT INTO sites(name,url) values(%s, %s)"
val = ("baidu", "www.baidu.com")

#my_cursor.execute(sql, val)

# 批量插入数据
multi_val = [
    ('Google', 'www.google.com'),
    ('Github', 'www.github.com'),
    ('python', 'www.python.org')
]

#my_cursor.executemany(sql, multi_val)

#db.commit()

# 查询所以数据
#my_cursor.execute("select * from sites")
# 必须先fetch
# 读取所以
#result_all = my_cursor.fetchall()
#print("all",result_all)

# 读取一条
#result_one = my_cursor.fetchone()
#print("one", result_one)

# 读取指定字段
#my_cursor.execute("select name, url from sites")
#part_result = my_cursor.fetchall()
#print(part_result)

# 删除记录
#delete_sql = "delete from sites where id=%s"
#delete_val = (2,)
#my_cursor.execute(delete_sql, delete_val)
#db.commit()
#print(my_cursor.rowcount)

# 更新记录
#update_sql = "update sites set name='GITHUB' where name='Github'"
#my_cursor.execute(update_sql)
#db.commit()

# 删除表
delete_table_sql = "drop table sites"
my_cursor.execute(delete_table_sql)


