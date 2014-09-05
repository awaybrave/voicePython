def process(word):
	print 'Process: ', word

filename = 'testByteByByte.txt'
# byte by byte
f = open(filename)
char = f.read(1)
while char:
	process(char)
	char = f.read(1)
f.close()

# one line at a time

f = open(filename)
while True:
	line = f.readline()
	if not line: break
	process(line)
f.close()

f = open(filename)
process(f.read())

f.close()

#iterate the file object
print list(open(filename))
f.close()

