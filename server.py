__author__ = 'snalam200'

from _socket import *


new_socket = socket()
host = gethostname()
port = 3333
socket_tuple = (host, port)
new_socket.bind(socket_tuple)
new_socket.listen(5)
new_socket.accept()
new_socket.send("Thanks for connecting")
new_socket.close()





