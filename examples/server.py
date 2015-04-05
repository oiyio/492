# http://stackoverflow.com/questions/7749341/very-basic-python-client-socket-example

import socket

def s():

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind(('localhost', 8089))
	serversocket.listen(5) # become a server socket, maximum 5 connections

	while True:
		connection, address = serversocket.accept()
		buf = connection.recv(64)
		if  (len(buf) > 0):
			print (buf)
			break


if __name__ == "__main__":
 # if you call this script from the command line (the shell) it will
 # run the 'main' function
	s()