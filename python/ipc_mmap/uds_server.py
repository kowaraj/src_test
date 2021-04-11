import socket
import sys
import os
import time
import threading 

server_address = './uds_socket'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise


# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to the port
print('starting up on {}'.format(server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(10)

def worker(socket_for_client):
    try:
        print('so = {}'.format(socket_for_client))
        print('connection from {}'.format(client_address))

        # Receive the data in small chunks and retransmit it
        while True:
            data = socket_for_client.recv(100)
            print('received: {}'.format(data))
            if len(data) == 0: 
                print('no more data, quit')
                break
            
    finally:
        # Clean up the connection
        print('closing the client socket')
        socket_for_client.close()
        


while True:
    # Wait for a connection
    print('waiting for a connection')
    socket_for_client, client_address = sock.accept()
    threading.Thread(target=worker, args=([socket_for_client])).start()

