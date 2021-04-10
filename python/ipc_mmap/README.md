A server-client pair using "Unix Domain Sockets"


[socket — Low-level networking interface](https://docs.python.org/3/library/socket.html)

From the programmer’s perspective there are two essential differences 
between using a Unix domain socket and an TCP/IP socket. 

First, the address of the socket is a path on the filesystem, 
rather than a tuple containing servername and port. 

Second, the node created in the filesystem to represent the socket 
persists after the socket is closed, and needs to be removed each time the server starts up. 


