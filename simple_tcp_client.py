#!/usr/bin/python3


import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("192.168.197.101", 6666))

print(s.recv(1024))
s.close()
