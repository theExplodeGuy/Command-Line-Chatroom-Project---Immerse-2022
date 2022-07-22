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
list_of_names = []
names_to_ip = {}

def clientthread(conn, addr):
    while True:
        name = conn.recv(2048).decode()
        if name in names_to_ip:
            conn.send(0)
        else:
            conn.send(1)
            break

    names_to_ip[name] = conn

    welcomemsg = 'Welcome to the chat room of immerse! ' + name + '\n'
    conn.send(welcomemsg.encode())
    conn.send('Online Users\n'.encode())
    for n in list_of_names:
        conn.send((n + '\n').encode())
    conn_msg = name + " Connected"
    broadcast(conn_msg, conn)

    while True:
        message = conn.recv(2048)

        print("<" + name + ">" + message.decode())

        # broadcast function to send the message to all users
        message_to_sent = "<" + name + ">" + message.decode()
        print(message_to_sent)
        if message.decode().strip() == 'stop':
            msg = name + ' Disconnected'
            broadcast(msg, conn)
            list_of_names.remove(name)
            conn.close()
            exit_thread()
        else:
            broadcast(message_to_sent, conn)

def broadcast(message, connection):
    for name in names_to_ip:
        if names_to_ip[name] != connection:
            try:
                print(message)
                if message == "<" + addr[0] + ">" + 'stop':
                    remove(name)
                else:
                    names_to_ip[name].sendall(message.encode())
            except:
                names_to_ip[name].close()
                remove(names_to_ip[name])

def remove(name):
    if name in names_to_ip:
        names_to_ip.pop(name)


while True:
    conn, addr = server.accept()

    print(addr[0] + " connected")

    # creates individual threat for every user that connects
    start_new_thread(clientthread, (conn, addr))

# conn.close()
# server.close()
