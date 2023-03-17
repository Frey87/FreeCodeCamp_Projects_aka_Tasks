#!/usr/bin/python3
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = input("Please enter the host name")
port_number = input("Please enter the port number")

host = gethostbyname(host_name)
port = port_number

clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.close()
print(message.decode("ascii"))
