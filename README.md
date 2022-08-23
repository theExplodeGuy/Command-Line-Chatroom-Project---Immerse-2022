Introduction
------------

A LAN chatroom application. Uses a client-server model wherein a server is hosted and then clients can connect to the server in order to transmit messages to other clients.

Installation
-------------

Libraries Used:
 - Sockets
 - Threading

Both libraries are built in so no extra installations are needed other than installing python 3.9.6

Usage
-----
###Server
- Run Server.py on a machine.
- Input that machine's IP and choose a port for the server to run on. 

###Client
- To connect to the server run Client.py and type in the IP address and the port of the server.

Commands:
The server supports 2 commands.

- ```!stop``` disconnects you from the server.
- ```!dm {Name of User you wish to DM} {Message you wish to send}``` Sends a user a message only they can see.
