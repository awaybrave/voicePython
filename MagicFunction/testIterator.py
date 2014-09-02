from Iterator import TestIterator
from Iterator import *

ti = TestIterator()
print list(ti)

nested = [[[3,4], [1]], [32,56], [1,3,5]]
for num in flatten(nested):
	print num
print list(flatten2(nested))

print list(flatten3([['foo', 'bar'], 'ddd']))
