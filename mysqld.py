# 导入模块
import pymysql

# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="test_db",
    charset="utf8")
# print(conn)
# print(type(conn))

# 获取连接下的游标
cursor_test = conn.cursor()
print(cursor_test)

# 使用 execute()  方法执行 SQL 查询，查询数据库版本
cursor_test.execute("SELECT VERSION()")


def get_by_name(name):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='test_db', charset='utf8')
    cursor = conn.cursor()
    sql = """select user_id,user_name,passwd from user where user_name like '{}';""".format(name)
    cursor.execute(sql)
    results = format_data(cursor.description, cursor.fetchall())
    cursor.close()
    conn.close()
    return results
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
print(get_by_name("jack"))
# 关闭数据库连接
conn.close()