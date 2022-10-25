#!/usr/bin/env python

import socket
#create socket
s = socket.socket

#open up a port
port = 1337
s.bind(('',port))

#put socket into listen mode
s.listen(5)

#listen as long as it's running
while True:
    #accept incoming connections
    c, addr = s.accept()

    #send next set of commands
    c.send('pwn all the things!')

    c.close