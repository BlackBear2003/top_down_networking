import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("192.168.31.183", 3000))
udp_socket.sendto(b"I am 3000", ("192.168.31.183", 8080))
while True:
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)
    if recv_data[0] == b"exit":
        break
    s = input("请输入要发送的数据：")
    udp_socket.sendto(s.encode(), ("192.168.31.183", 8080))