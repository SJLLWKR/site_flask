import pymysql


def get_by_name(name):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='test_db', charset='utf8')
    cursor = conn.cursor()
    sql = """select user_id,user_name,passwd from user where user_name like '{}';""".format(name)
    cursor.execute(sql)
    results = format_data(cursor.description, cursor.fetchall())
    cursor.close()
    conn.close()
    return results
def get_by_name_all():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='test_db', charset='utf8')
    cursor = conn.cursor()
    sql = """select * from user;"""
    cursor.execute(sql)
    results = format_data(cursor.description, cursor.fetchall())
    cursor.close()
    conn.close()
    return tuple(results)
# 数据格式化 fields 字段名，result 结果集
def format_data(fields, result):
    # 列字段数组 格式['name', 'password']
    field = []
    for i in fields:
        field.append(i[0])
    # 返回的数组集合 格式[{'id': 1, 'name': 'admin', 'password': '123456'}]
    results = []
    for res in result:
        line_data = {}
        for index in range(0, len(field)):
            line_data[field[index]] = res[index]
        results.append(line_data)
    return results
def addUser(name,passwd):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='test_db', charset='utf8')
    cursor = conn.cursor()
    sql1 = """insert into user(user_name,passwd) values ('{}','{}');""".format(name,passwd)
    sql2 = """SET @i=0;"""
    sql3 = """UPDATE user SET user_id=(@i:=@i+1);"""
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    conn.commit()
    cursor.close()
    conn.close()
    return 'ok'
def deleteUser(name):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='test_db', charset='utf8')
    cursor = conn.cursor()
    sql1 = """delete from user where user_name = '{}';""".format(name)
    sql2 = """SET @i=0;"""
    sql3 = """UPDATE user SET user_id=(@i:=@i+1);"""
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    conn.commit()
    cursor.close()
    conn.close()
    return 'ok'
def changeUser(password,name):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='test_db', charset='utf8')
    cursor = conn.cursor()
    sql1 = """UPDATE user set passwd='{}' where user_name = '{}';""".format(password,name)
    cursor.execute(sql1)
    conn.commit()
    cursor.close()
    conn.close()
    return 'ok'


#workspace
def wks_get_by_name_all():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='test_db', charset='utf8')
    cursor = conn.cursor()
    sql = """select * from workspace;"""
    cursor.execute(sql)
    results = format_data(cursor.description, cursor.fetchall())
    cursor.close()
    conn.close()
    return tuple(results)