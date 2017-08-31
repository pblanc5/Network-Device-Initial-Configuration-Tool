# Author: Patrick Blanchard
# Contact: pblanc5@lsu.edu --or-- patrickblanchard.dev@gmail.com
# Description: Dummy server to return data send to it.
#

import socket

class TestServer():

    def __init__(self, port):
        self.port = port

    def start_server(self):
        HOST = '127.0.0.1'
        PORT = 3000 + self.port

        s = socket.socket(socket.AF_INET)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        while True:
            data = conn.recv(5000)
            if not data:
                break
        conn.close()
        return data.split('\n')
