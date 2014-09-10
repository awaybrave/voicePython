# a simple server-client connection example using socket.  
#server: 
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
	c.close()

# and client: 
s = socket.socket() 
host = socket.gethostname()
port = 1234 
s.connect((host, port)) 
print s.recv(1024)

#socket.accept is a syschronious api.

#Urllib and Urllib2 
#the libraries helps a lot like reading a remote file like a local file
import urllib
webpage = urllib.urlopen('http://www.baidu.com')
text = webpage.read() # readlines, readline just like a local file
#or retrieve a remote file and save it locally.
urllib.urlretrieve('http://python.org', 'python.html')

#SocketServer Framework(contains several classes, tcp and udp)
from SocketServer import TCPServer, StreamRequestHandler
class Handler(StreamRequestHandler):
	def handle(self):
		addr = self.request.getpeername()
		print 'Got connection from ', addr
		self.wfile.write('Thank you for connecting')

#singleton
server = TCPServer(('', 1234), Handler)
server.serve_forever() #while True statement in minimalServer.py
#the above program serves as a server and minimalClient.py can connect it.

#forking to make an independent process to deal with the connection
from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler
#forking mode
class Server(ForkingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):
	def handle(self):
		addr = self.request.getpeername()
		print 'Got connection from ', addr
		self.wfile.write('Thank you for connecting')
server = Server(('', 1234), Handler)
server.serve_forever()

#threading to deal with the connection
#make the server inherent from ThreadingMixIn
class Server(ThreadingMixIn, TCPServer)

#dealing with large amount of clients: hear them a little and 
#then put it back in the line with others. There are two ways to 
#do that: poll(more scalable but only available in UNIX) and select
#both of which from select module.

# in mac: there is no poll in select module
