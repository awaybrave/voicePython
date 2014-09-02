# descriptor: http://users.rcn.com/python/download/Descriptor.htm
__metaclass__ = type
class Rectangle:
	def __init__(self):
		self.width = 0
		self.height = 0
	def setSize(self, size):
		self.width, self.height = size
	def getSize(self):
		return self.width, self.height	

	# getitem, setitem
	size = property(getSize, setSize)
