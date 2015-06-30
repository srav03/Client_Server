__author__ = 'snalam200'

from _socket import *


new_socket = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 33333
socket_tuple = (host, port)
new_socket.bind(socket_tuple)
new_socket.listen(5)
connection, client_address = new_socket.accept()
new_socket.send("Thanks for connecting")
new_socket.close()
connection.close()





