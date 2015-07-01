__author__ = 'snalam200'

from _socket import *


new_socket = socket(AF_INET, SOCK_STREAM)
#host = gethostbyaddr('localhost')
port = 33347
socket_tuple = ('localhost', port)
#new_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
new_socket.bind(socket_tuple)
new_socket.listen(5)
connection, client_address = new_socket.accept()
print ("Connection received from client: '%s'" % format(client_address))
connection.send("Thanks message from server")
#new_socket.close()
connection.close()





