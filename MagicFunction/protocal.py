__metaclass__ = type

def checkIndex(key):
	if not isinstance(key, (int, long)): raise KeyError
	if key < 0: raise IndexError 

class ArithmeticSequence:
	def __init__(self, start=0, step=1):
		self.start = start
		self.step = step
		self.changed = {}

	def __getitem__(self, key):
		checkIndex(key)
		try: return self.changed[key]
		except KeyError:
			return self.start + self.step*key
	
	def __setitem__(self, key, value):
		checkIndex(key)
		self.changed[key] = value 

	def __delitem__(self, key):
		checkIndex(key)
		if key in self.changed:
			del self.changed[key]

# We can also subclass a built-in class like list or dict. But doing this means the newly created class inherit from object and that makes the class a new-style one.

class CounterList(list):
	def __init__(self, *args):
		super(CounterList, self).__init__(*args)
		self.counter = 0
	def __getitem__(self, key):
		self.counter = self.counter + 1
		return super(CounterList, self).__getitem__(key)
