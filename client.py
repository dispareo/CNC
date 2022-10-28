#!/usr/bin/env python
import socket

#create socket object
s = socket.socket()

port = 1337

s.connect(('127.0.0.1', port))
print(s.recv(1024))
s.close
