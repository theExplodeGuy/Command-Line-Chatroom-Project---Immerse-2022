import socket, sys, select
port = 8080
connect_address = input("Enter IP Address\n")

ip_list = connect_address.split('.')
if len(ip_list) == 4:
    for x in ip_list:
        if int(x) > 255 or int(x) < 0:
            print("that's not how IPs work my guy . . . ")
            exit()
else:
    print("Study ur networking :/")
    exit()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((connect_address,port))
def main_loop():
    while True:
        sockets_list = [sys.stdin, server]
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

        for socks in read_sockets:
                if socks == server:
                    message = socks.recv(2048)
                    print(message)
                else:
                    message = sys.stdin.readline()
                    server.send(message.encode())
                    sys.stdout.write("<You> ")
                    sys.stdout.write(message)
                    sys.stdout.flush()
                    if message == "stop":
                        return

main_loop()
server.close()