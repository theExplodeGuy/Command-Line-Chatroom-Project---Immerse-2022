import socket, sys, select

connect_address = input("Enter IP Address: ")

ip_list = connect_address.split('.')
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
        port = int(input('Select Port: '))
        if port <= 65535:
            break
        else:
            print("Study ur networking :/")
    except:
        pass

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((connect_address, port))
while True:
    server.send(input("What is your name? ").encode().strip())
    condition = server.recv(1024).decode()
    if bool(int(condition)):
        print('name accepted')
        break
    print("Name already taken, choose a new name.")

while True:
    sockets_list = [sys.stdin, server]
    """Stops from hanging on receiving data from the server"""
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048).decode()
            print(message)
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
            sys.stdout.write("<You> ")
            sys.stdout.write(message)
            sys.stdout.flush()
            if message.strip() == "!stop":
                server.close()
                exit()
