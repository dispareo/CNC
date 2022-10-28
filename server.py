#!/usr/bin/env python

import socket
s = socket.socket()
port = 1337
s.bind(('', port))

#put socket into listen mode
s.listen(5)

#listen as long as it's running
while True:
    #accept incoming connections
    c, addr = s.accept()
    c.send(b,'Mark Bayley')
    c.close
