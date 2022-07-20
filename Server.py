import socket
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_address = input('Input an IP address: ')

while True:
    try:
        Port = int(input('Select Port: '))
        break
    except:
        pass

server.bind((IP_address, Port))

"""listen for 50 active connections. This number can be modified"""
server.listen(50)

list_of_clients = []


def clientthread(conn, addr):
    welcomemsg = 'Welcome to the chat room of immerse! ' + addr[0]
    conn.send(welcomemsg.encode())

    while True:
        message = conn.recv(1024)

        print("<" + addr[0] + ">" + message.decode())

        # broadcast function to send the message to all users
        message_to_sent = "<" + addr[0] + ">" + message.decode()
        print(message_to_sent)
        broadcast(message_to_sent.encode(), conn)



def broadcast(message, connection):
    print(list_of_clients)
    for clients in list_of_clients:
        print(clients)
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()

    list_of_clients.append(conn)

    print(addr[0] + " connected")

    # creates individual threat for every user that connects
    start_new_thread(clientthread, (conn, addr))

# conn.close()
# server.close()
