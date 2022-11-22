from flask import *
from flask import Flask
from flask import request
import user_dao
import user_mysql
import connserver

app = Flask(__name__)  # 初始化app


@app.route('/', methods=['GET', 'POST'])  # 建立路由
def login():
    return render_template('login.html')  # 定义路由执行结果


@app.route('/navigationu', methods=['GET', 'POST'])  # 建立路由
def login_res():
    if request.method == 'POST':
        username = request.values.get('username')
        passwd = request.values.get("password")
        return user_dao.login_dao(username, passwd)


@app.route('/navigationu.html', methods=['GET', 'POST'])  # 建立路由
def navigationu():
    return render_template('navigationu.html')  # 定义路由执行结果


@app.route('/navigation.html', methods=['GET', 'POST'])  # 建立路由
def navigation():
    return render_template('navigation.html')  # 定义路由执行结果


@app.route('/mulog.html', methods=['GET', 'POST'])  # 建立路由
def mulog():
    return render_template('mulog.html')  # 定义路由执行结果


@app.route('/muser.html', methods=['GET', 'POST'])  # 管理员页面
def muser():
    return render_template('muser.html', slist=user_mysql.get_by_name_all())  # 定义路由执行结果


@app.route('/addUser', methods=['GET', 'POST'])  # 管理员页面，增加普通用户
def adduser():
    if request.method == 'POST':
        username = request.values.get('username')
        passwd = request.values.get("password")
        print(username,passwd)
        return user_mysql.addUser(username, passwd)


@app.route('/deleteUser', methods=['GET', 'POST'])  # 管理员页面，删除
def deleteuser():
    if request.method == 'POST':
        username = request.values.get('username')
        print(username)
        return user_mysql.deleteUser(username)

@app.route('/changeUser', methods=['GET', 'POST'])  # 管理员页面，删除
def changeUser():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        print(password,username)
        return user_mysql.changeUser(password,username)

@app.route('/getUser', methods=['GET', 'POST'])  # 管理员页面，增加普通用户
def getuser():
    return json.dumps(user_mysql.get_by_name_all()) # 定义路由执行结果



#workspace

@app.route('/workspace.html', methods=['GET', 'POST'])  # 管理员页面
def workspace():
    return render_template('workspace.html',wklist=user_mysql.wks_get_by_name_all())  # 定义路由执行结果


@app.route('/getWork', methods=['GET', 'POST']) # 管理员页面，增加普通用户
def getWork():
    return json.dumps(user_mysql.wks_get_by_name_all()) # 定义路由执行结果

@app.route('/wkchange', methods=['GET', 'POST'])  # 管理员页面，删除
def wkchange():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        print(password,username)
        #return user_mysql.changeUser(password,username)
@app.route('/getfactory', methods=['GET', 'POST'])  # 管理员页面，增加普通用户
def getfactory():
    if request.method == 'POST':
        ip = request.values.get('ip')
        data = connserver.connserver(ip)
        print(data)
        return data
if __name__ == '__main__':
    app.run(debug=True)  # 运行app
