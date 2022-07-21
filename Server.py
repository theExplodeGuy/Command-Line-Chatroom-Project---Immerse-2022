import socket
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_address = input('Input an IP address: ')
ip_list = IP_address.split('.')
if len(ip_list) == 4:
    for x in ip_list:
        if int(x) > 255 or int(x) < 0:
            print("that's not how IPs work my guy . . . ")
            exit()
else:
    print("Study ur networking :/")
    exit()

while True:
    try:
        Port = int(input('Select Port: '))
        if Port <= 65535:
            break
        else:
            print('Study your Networking :/')
    except:
        print('Study your Networking :/')


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

        # broadcast function to send the message to all users
        message_to_sent = "<" + client_name + ">" + message.decode()
        broadcast(message_to_sent, conn)

        if message.decode().strip() == 'stop':
            msg = client_name + 'disconnected'
            broadcast(msg, conn)
            conn.close()
            exit_thread()
        else:
            broadcast(message_to_sent, conn)


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
        connection.close()


while True:
    conn, addr = server.accept()

    list_of_clients.append(conn)

    print(addr[0] + " connected")

    # creates individual threat for every user that connects
    start_new_thread(clientthread, (conn, addr))

# conn.close()
# server.close()
