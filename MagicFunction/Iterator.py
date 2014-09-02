__metaclass__ = type
class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def next(self):
		self.a, self.b = self.b, self.a+self.b
		return self.a 
	def __iter__(self):
		return self

# we can make sequences from iterators
# value is self.value
class TestIterator:
	value = 1
	def next(self):
		self.value += 1
		if self.value > 10: raise StopIteration
		return self.value
	def __iter__(self):
		return self
#By using the above example, we can make some generators.
#A generator is a kind of iterator that is defined with normal syntax.

def flatten(nested):
	for row in nested:
		for col in row:
			yield col
# yield statement stop the current flatten function and "return" the current yielded element and waits to be reawakened.

#recursive yield function 
def flatten2(nested):
	try:
		#there has to be two loops for reducing the recursive case.
		for sublist in nested:
			for element in flatten2(sublist):
				yield element
	except TypeError:
		yield nested

# but what if the element is string

def flatten3(nested):
	try:
	# Don't iterate over string-like objects:
		try: nested + ''	
		except TypeError: pass
		else: raise TypeError
		for sublist in nested:
			for element in flatten3(sublist):
				yield element
	except TypeError:
		yield nested
