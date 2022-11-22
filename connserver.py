def connserver(IP):
    # -*- encoding: utf-8 -*-
    # 半双工循环发送
    import socket
    import sys

    # IP = '127.0.0.1'  # 填写服务器端的IP地址
    # IP = 'localhost'  # 填写服务器端的IP地址
    # IP填写服务器端的IP地址
    port = 4242  # 端口号必须一致
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((IP, port))
    except Exception as e:
        print('server not find or not open')
        sys.exit()
    while True:
        trigger = 'input("史艳翠:")'
        s.sendall(trigger.encode())
        data = s.recv(1024)
        s.close()
        data = data.decode()
        #print('乐乐:', data)
        if trigger.lower() == '1':  # 发送1结束连接
            break
        return data
