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
    client_name = conn.recv(2048).decode()
    print(client_name)
    welcomemsg = 'Welcome to the chat room of immerse! ' + client_name
    conn.send(welcomemsg.encode())

    while True:
        message = conn.recv(2048)

        print("<" + client_name + ">" + message.decode())

        # broadcast function to send the message to all users
        message_to_sent = "<" + client_name + ">" + message.decode()
        print(message_to_sent)
        broadcast(message_to_sent, conn)



def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                print(message)
                if message == "<" + addr[0] + ">" + 'stop':
                    remove(clients)
                else:
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
