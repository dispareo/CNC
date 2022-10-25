#!/usr/bin/env python

import socket

#create socket object
s = socket.socket

#open the port on the server
port = 1337


#connect to the client and receive message
s.connect(('127.0.0.1', port))
print s.recv(1024)
s.close