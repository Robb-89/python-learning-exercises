#!/usr/bin/python3
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.197.101", 8888))
print(s.recv(1024).decode())
response=s.recv(1024).decode()

# Please add the first two numbers given and multiply the last to that total: (a+b)*c
# This must be completed within 3 seconds.
# First: 5
# Second: 9
# Third: 16
numbers = []

for line in response.split():
    if line.isnumeric():
        numbers.append(line)


sum = (int(numbers[1]) + int(numbers[2])) * int(numbers[3])
s.send(str(sum).encode())
print(s.recv(1024).decode())
s.close()
