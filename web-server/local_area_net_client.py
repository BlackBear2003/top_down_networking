import socket

HOST = '192.168.31.183'  # 服务器的IP
PORT = 12306  # 设置端口
# 创建一个socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


while True:
    # 接受控制台的输入
    data = input()
    # 对数据进行编码格式转换，不然报错
    data = data.encode('utf-8')
    # 如果输入quit则退出连接
    if data == b'quit':
        print(b'connect quit.')
        break
    else:
        # 发送数据
        client.sendall(data)
        # 接收服务端的反馈数据
        rec_data = client.recv(1024)
        print(b'form server receive:' + rec_data)

# 发送数据告诉服务器退出连接
client.sendall(b'quit')
client.close()
