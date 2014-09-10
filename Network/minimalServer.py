import pdb
import socket
s = socket.socket()

host = socket.gethostname() 
port = 1234 
s.bind((host, port))

s.listen(5)
while True:
	#pdb.set_trace()
	# s.accept blocks the normal executing stream
	# until it receives a connection request.
	c, addr = s.accept()
	print 'Got connection from', addr
	c.send('Thank you fro connecting')

#Question: What if we want to run server twice in the same time ?
#Answer: Then python raises the socket error for the port number is
#already occupied by another program.
	c.close()
