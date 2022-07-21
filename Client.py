import socket, sys, select
connect_address = input("Enter IP Address: ")
connect_port = int(input("Enter port: "))

ip_list = connect_address.split('.')
if len(ip_list) == 4:
    for x in ip_list:
        if int(x) > 255 or int(x) < 0:
            print("that's not how IPs work my guy . . . ")
            exit()
else:
    print("Study ur networking :/")
    exit()

if connect_port > 65535 or connect_port < 1024:
    print("so you just don't know how ports work, huh?")
    exit()

name = input("What is your name? ")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((connect_address,connect_port))

server.send(name.encode())

while True:
    sockets_list = [sys.stdin, server]
    """Stops from hanging on receiving data from the server"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048).decode()
            else:
                message = sys.stdin.readline()
                server.send(message.encode())
                sys.stdout.write("<You> ")
                sys.stdout.write(message)
                sys.stdout.flush()

