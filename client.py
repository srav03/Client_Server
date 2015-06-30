__author__ = 'snalam200'

from socket import *


client_socket = socket()
host = gethostname()
port = 3333
socket_tuple = (host, port)
client_socket.connect(socket_tuple)
client_socket.close



