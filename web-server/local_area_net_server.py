import socket

HOST = '192.168.31.183'  # 服务器的IP
PORT = 12306  # 设置端口
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定监听端口，localhost和127.0.0.1是本机之间的进程通信使用的
server.bind((HOST, PORT))
# 开始监听，并设置最大连接数
server.listen(5)

print(u'waiting for connect...')
# 等待连接，一旦有客户端连接后，返回一个建立了连接后的套接字和连接的客户端的IP和端口元组
connect, (host, port) = server.accept()
print(u'the client %s:%s has connected.' % (host, port))

while True:
    # 接受客户端的数据
    data = connect.recv(1024)
    # 如果接受到客户端要quit就结束循环
    if data == b'quit' or data == b'':
        print(b'the client has quit.')
        break
    else:
        print(b'the client say:' + data)
        # 发送数据给客户端
        s = input("recall:")
        connect.sendall(s.encode())

# 结束socket
server.close()
