import socket
import sys
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
serverPort = 8080
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('server started!')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048).decode()

        print(message)

        OkMSG = "HTTP/1.1 200 OK \r\n\r\n"
        connectionSocket.send(OkMSG.encode())
        connectionSocket.send('hello world'.encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        ErrMSG = 'HTTP/1.1 404 Not Found \r\n\r\n'
        connectionSocket.send(ErrMSG.encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Close client socket
        connectionSocket.close()
        break

serverSocket.close()
sys.exit()
