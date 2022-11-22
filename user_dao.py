import user_mysql, user_model

def login_dao(name, password):
    if len(user_mysql.get_by_name(name)) > 0:
        res = user_mysql.get_by_name(name)[0]
        print(res)
        user = user_model.User(i_d=res['user_id'], name=res['user_name'], password=res['passwd'])
        print(user.password)
        if user.name == name and user.password == password:
            return 'ok'
        else:
            return 'mu'
    return '用户名不存在'

