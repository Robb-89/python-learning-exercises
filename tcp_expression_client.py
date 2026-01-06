#!/usr/bin/python3

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("192.168.197.101", 8888))

print(s.recv(1024).decode())
s.send("(6+7)*5".encode())
print(s.recv(1024).decode())
s.close()

