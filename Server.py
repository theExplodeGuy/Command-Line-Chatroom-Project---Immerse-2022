import socket
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_address = input('Enter IP address: ')

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
            print("Study ur networking :/")
    except:
        pass

server.bind((IP_address, Port))

"""listen for 50 active connections. This number can be modified"""
server.listen(50)

list_of_clients = []
list_of_name = []


def clientthread(conn, addr):
    name = conn.recv(2048).decode().strip()
    list_of_name.append(name)
    welcomemsg = 'Welcome to the chat room of immerse! ' + name + '\n'
    conn.send(welcomemsg.encode())
    online_name(conn)

    while True:
        message = conn.recv(2048)

        print("<" + name + ">" + message.decode())

        # broadcast function to send the message to all users
        message_to_sent = "<" + name + ">" + message.decode()
        print(message_to_sent)
        if message.decode().strip() == 'stop':
            msg = name + ' Disconnected'
            broadcast(msg, conn)
            remove_name(name)
            conn.close()
            exit_thread()
        else:
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


def remove_name(name):
    if name in list_of_name:
        list_of_name.remove(name)


def online_name(connection):
    connection.send("Online Users:\n".encode())
    for name in list_of_name:
        online_msg = 'Online: ' + name + '\n'
        connection.send(online_msg.encode())


while True:
    conn, addr = server.accept()

    list_of_clients.append(conn)

    print(addr[0] + " connected")

    # creates individual threat for every user that connects
    start_new_thread(clientthread, (conn, addr))

# conn.close()
# server.close()
