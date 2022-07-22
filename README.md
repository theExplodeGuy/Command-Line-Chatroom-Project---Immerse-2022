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

Run Server.py on a machine, inputting that machine's IP 
To connect to the server run Client.py and type in that IP address and the port it is using to be able to chat with others.

Commands:
There are 2 commands that can be used currently

- ```!stop``` disconnects you from the server
- ```!dm {Name of User you wish to DM} {Message you wish to send}``` Sends a user a message only they can see
