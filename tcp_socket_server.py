#!/usr/bin/python3


import socket 
import threading 

host = "192.168.45.182"
port = 8080
     
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(4)
print('Server is listening for incoming connections')
     


while True:
#accept connections from outside
    conn,addr = server.accept()
    print("Connection Received from %s" % str(addr))
    data = conn.recv(1024)
    if not data: continue
    print(data)
    
server.close()

