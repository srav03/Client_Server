__author__ = 'snalam200'

from socket import *


client_socket = socket(AF_INET, SOCK_STREAM)

#host = gethostbyaddr('localhost')
port = 33347
socket_tuple = ('localhost', port)
client_socket.connect(socket_tuple)
data_from_server = "Thanks message from server"
recv_size = 0
while True:
    if len(data_from_server) > recv_size:
        print client_socket.recv(16)
        recv_size += 16
    else:
        break
client_socket.close()



