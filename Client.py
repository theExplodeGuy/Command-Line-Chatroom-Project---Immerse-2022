"""
# echo-client.py

import socket

HOST = "192.168.30.91"  # The server's hostname or IP address
PORT = 1234  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"ls")

    data = s.recv(1024)

print(f"Received {data.decode('utf-8')}")
"""
import socket
import struct

class MySocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        self.sock.sendall(msg.encode())

    def receive(self):

        chunks = []
        while True:
            # Keep reading while the client is writing.
            data = self.sock.recv(1024)
            if not data:
                # Client is done with sending.
                break
            chunks.append(data.decode())

        self.sock.close()
        return chunks

sock = MySocket()
sock.connect('localhost', 1235)
sock.send('ls')
print(sock.receive())


