# coding: utf-8

# 使用PyMysql连接Mysql (python3)
import pymysql

# 连接数据库
db = pymysql.connect('192.168.28.48', 'root', '123456', 'test')

# 创建一个游标对象Cursor
db_cursor = db.cursor()

# 使用execute()执行sql
db_cursor.execute("select VERSION()")

# 获取单条数据
data = db_cursor.fetchone()
print("mysql version:%s" % data)

# 创建表
db_cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """
        CREATE TABLE EMPLOYEE(
            firstName char(20) NOT NULL,
            lastName char(20),
            age int,
            sex char(1),
            income float
        )
        """
db_cursor.execute(sql)

# 插入数据
insert_sql = """
                INSERT INTO EMPLOYEE(firstName, lastName, age, sex, income) values('Windows', 'Linux', 12, 'M', 20000)
            """
db_cursor.execute(insert_sql)

try:
    # 执行语句
    db_cursor.execute(insert_sql)
    # 提交到数据库执行
    db.commit()
except:
    # 出现异常，则回滚
    db.rollback()

# 查询数据
"""
    fetchone(): 获取下一个查询结果集，结果集是一个对象
    fetchall(): 接收全部的返回结果行
    rowcount: 只读属性，并返回执行execute()方法后影响的行数
"""

query_sql = "SELECT * FROM EMPLOYEE \
            WHERE income > %s" % (1000)

try:
    # 执行语句
    db_cursor.execute(query_sql)
    # 获取所有结果
    results = db_cursor.fetchall()
    for row in results:
        firstName = row[0]
        lastName = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("firstName=%s, lastName=%s, age=%s, sex=%s, income=%s" % (firstName, lastName, age, sex, income))
except:
    print('No Data')

# 更新数据
update_sql = "UPDATE EMPLOYEE set income = 30000 where firstName='%s'" % ('Windows')

try:
    # 执行语句
    db_cursor.execute(update_sql)
    # 提交到数据库执行
    db.commit()
except:
    # 执行失败，回滚操作
    db.rollback()

# 删除数据
delete_sql = "DELETE FROM EMPLOYEE where lastName='%s'" % ('Linux')
try:
    # 执行语句
    db_cursor.execute(delete_sql)
    # 提交到数据库执行
    db.commit()
except:
    # 执行失败，回滚操作
    db.rollback()

# 关闭数据库
db.close()
