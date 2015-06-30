__author__ = 'snalam200'

from socket import *


client_socket = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 33333
socket_tuple = (host, port)
client_socket.connect(socket_tuple)
print client_socket.recv()
client_socket.close()



