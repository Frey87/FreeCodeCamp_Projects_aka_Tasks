#!/usr/bin/python3
import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = input("Please enter the host name")
port_number  = int(input("Please enter the port number"))

host = socket.gethostbyname(host_name)
port = port_number

serversocket.bind(host, port)

serversocket.listen(3)

while True:
  clientsocket, address = serversocket.accept()
  print("received connection from: %s" % str(address))
  message = "Thank you for connecting to this server" + "\r\n"
  clientsocket.send(message.encode("ascii"))
  
  clientsocket.close()
