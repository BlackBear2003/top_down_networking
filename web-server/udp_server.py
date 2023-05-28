import socket

HOST = '10.194.4.73'

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, 8080))

udp_socket.sendto(b"I am 8080", (HOST, 3000))
while True:
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)
    if recv_data[0] == b"exit":
        break
    s = input("请输入要发送的数据：")
    udp_socket.sendto(s.encode(), (HOST, 3000))

