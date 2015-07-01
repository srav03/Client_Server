__author__ = 'snalam200'

from socket import *


client_socket = socket(AF_INET, SOCK_STREAM)

#host = gethostbyaddr('localhost')
port = 33345
socket_tuple = ('localhost', port)
client_socket.connect(socket_tuple)
for i in range(1, len("Thanks message from server")):
    print client_socket.recv(16)
    else:
        break
client_socket.close()



