"""
# echo-server.py

import socket
import time
import os
import struct

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 1235  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            time.sleep(1)
            files = os.listdir()
            time.sleep(1)
            msg = struct.pack('>I', 2) + bytes('hi', 'utf-8')
            print(msg)
            s.sendall(msg)
"""

import socket
import os

# next create a socket object
import time

s = socket.socket()
print("Socket successfully created")


port = 1235
s.bind(('', port))
print("socket binded to %s" % (port))


s.listen(5)
print("socket is listening")

chunks = []
while True:

    c, addr = s.accept()
    files = os.listdir()

    data = c.recv(1024)
    if not data:
        # Client is done with sending.
        break
    chunks.append(data.decode())
    print(chunks)

    if data.decode() == 'ls':
        for file in files:
            c.sendall(file.encode())
            time.sleep(0.5)

    print('Got connection from', addr)


    break