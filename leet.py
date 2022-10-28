import threading
import socket
import ssl
import http.server
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

s = socket.socket()

def connect():
    #fucntion to keep serving up that 1337
    #create the name + date header
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            today = datetime.date.today()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(f"Mark Bayley {today}", "utf-8"))
               

    httpd = HTTPServer(('', (int(sys.argv[1]))), MyHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile='server.crt',
                                keyfile='server.key',
                               ssl_version=ssl.PROTOCOL_TLS)
    httpd.serve_forever()

    
   #while(True):
   #(clientConnection, clientIP) = secureServerSocket.accept();
    #    temp = random.uniform(50, 65);
     #   tempStr = "Temperature in the city is %2.2f"%temp;
      #  encoded = tempStr.encode();
       # clientConnection.sendall(encoded);
       # print("Replied to %s with the temperature value %2.2f"%(clientIP, temp));


 
def run_http():
    # function to serve up on HTTP
    server_address = ('', (int(sys.argv[2])))
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()



def run_https():
    #function to run https server
    server_address = ('', (int(sys.argv[3])))
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile='server.crt',
                                keyfile='server.key',
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
    
