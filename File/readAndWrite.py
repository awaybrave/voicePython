import pdb 
f = open('test.txt', 'w') 
f.write('Hello')
f.write('World')
#pdb.set_trace()
# writing is not done until close method is called.
f.close()

f = open('test.txt', 'r')
print f.read(4)
print f.read()
