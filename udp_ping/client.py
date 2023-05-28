from socket import *
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
clientSocket.bind(('', 12001))
clientSocket.settimeout(1)


def ping(i):

    send_time = time.time()
    # print(f"{i} send_time :{send_time}")
    clientSocket.sendto("hello,world".encode(), ("localhost", 12000))

    return send_time


def main():
    i = 1
    while i <= 10:
        send_time = ping(i)

        try:
            message, address = clientSocket.recvfrom(1024)
        except Exception:
            print(f"{i} package lost!")
            i = i + 1
            continue

        recv_time = time.time()

        # print(f"{i} recv_time :{recv_time}")
        print(f"{i} RTT = {(recv_time - send_time) * 1000} ms")

        i = i + 1


main()
