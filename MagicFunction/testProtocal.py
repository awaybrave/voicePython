# import ArithmeticSequence but not checkIndex works because ArithmeticSequence 
# is an interface that expose to this file.
from protocal import ArithmeticSequence
from protocal import checkIndex
from protocal import CounterList

a = ArithmeticSequence(1, 2)
print a[4]
a[4] = 2
print a[4]
print a[5]
del a[4]
print a[4]
print checkIndex(3)
#print checkIndex('a')

#cl = CounterList(1,2,3,4)
cl = CounterList()
cl.append(1)
cl.append(2)
cl.append(3)
print cl[1]
print cl.counter

cl2 = CounterList(range(10))
cl2.reverse()
print (cl2[2])
print (cl2[3])
print cl2.counter
print cl2
