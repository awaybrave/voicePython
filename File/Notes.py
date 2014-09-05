#Files:

# open function opens a file and returns a file object
# one mandatory argument: filename, mode and buffer are optional.
filename = "test.txt"
try:
	fileobj = open(filename)
except IOError:
	print "no file named %s" % filename

# file mode:
# w, r, a, b, +
# b stands for binary. 
# in Unix, the newline character is \n, but in Window, it is \r\n,
# while in Macintosh is \r, openning a text file in normal mode
# instead of binary mode, Python do the conversion automatically.
# So we can choose binary mode to prevent Python changing the source
# file.

# Buffering (set 1 to default caching value.)

# Reading and Writing
f = open('test.txt', 'w') 
f.write('Hello')
f.write('World')
f.close()

# Standard io is a subset of file object in Python. It has three 
# standard channel- stdin, stdout, stderr, since it is a file-like
# object, read and write methods are callable on sys.stdin or 
# sys.stdout.
text = sys.stdin.read()
# in UNIX command: cat file.txt | python fileLikeIO.py, the cat result is 
# passed to python standard input.

# in the examples above, files are treated as stream. But it can be accessed
# randomly.
#seek(offset[,whence]) offset is a byte count

#reading and writing with lines 
def process(word):
	print 'Process: ', word

#Doing byte and byte
filename = 'testByteByByte.txt'
f = open(filename)
char = f.read(1)
while char:
	process(char)
	char = f.read(1)
f.close()

#one line at a time
f = open(filename)
while True:
	line = f.readline()
	if not line: break
	process(line)

# do everthing
f.read() 
#or
f.readlines()
f.close()
# file object is iterable! 
print list(open(filename))
