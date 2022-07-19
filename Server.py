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
s = socket.socket()
print("Socket successfully created")


port = 12345
s.bind(('', port))
print("socket binded to %s" % (port))


s.listen(5)
print("socket is listening")

while True:

    c, addr = s.accept()
    files = os.listdir()


    for file in files:
        file += '\n'
        c.sendall(file.encode())

    print('Got connection from', addr)

    c.send('Thank you for connecting'.encode())
    c.close()

    break