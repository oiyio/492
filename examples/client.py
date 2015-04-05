# http://stackoverflow.com/questions/7749341/very-basic-python-client-socket-example

import socket

def c():

	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect(('localhost', 8089))
	clientsocket.send(bytes("hello from client", 'UTF-8'))
	
if __name__ == "__main__":
 # if you call this script from the command line (the shell) it will
 # run the 'main' function
	c()
	
	
# If you use Python3x then string is not the same type as for Python 2.x, you must cast it to bytes (encode it).
# bytes("hello from client")  -> string to byte conversion