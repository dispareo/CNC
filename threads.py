import threading
import socket
import ssl
import http.server

s = socket.socket()

def connect():
    #fucntion to keep serving up that 1337
    port = 1337
    s.bind(('',port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        c.send('Myah Bayley')
        c.close()
 
def run_http():
    # function to serve up on HTTP
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()



def run_https():
    #function to run https server
    server_address = ('localhost', 4443)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile='cert.pem',
                                keyfile='key.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
    httpd.serve_forever()

if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=connect)
    t2 = threading.Thread(target=run_http)
    t3 = threading.Thread(target=run_https) 
    


    # starting threads
    t1.start()
    t2.start()
    t3.start()
    
