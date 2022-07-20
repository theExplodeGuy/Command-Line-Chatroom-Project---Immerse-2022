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
        try:
            message = conn.recv(1024)
            print(message)
            if message:
                print("<" + addr[0] + ">" + message)

                # broadcast function to send the message to all users
                message_to_sent = "<" + addr[0] + ">" + message
                print(message_to_sent)
                broadcast(message_to_sent, conn)

            else:
                remove(conn)
        except:
            continue


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.sendall(message.encode())
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
