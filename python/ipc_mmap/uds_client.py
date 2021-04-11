import socket
import sys
import time

timeout = 100

while True:
    # Create a UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    print("running the job..... ")
    time.sleep(1)

    # Connect the socket to the port where the server is listening
    server_address = './uds_socket'
    print('connecting to {}'.format(server_address))
    try:
        sock.connect(server_address)
    except socket.error as msg:
        print("Connection error: {}".format(msg))
        continue

    try:
        print('sleep before sending')
        time.sleep(timeout)
        message = sys.argv[1] #'aaaaabbbbbcccccddddd'
        print('sending {}'.format(message))
        sock.sendall(message.encode())
    finally:
        print('closing socket')
        print('sleep before closing')
        time.sleep(timeout)
        sock.close()
