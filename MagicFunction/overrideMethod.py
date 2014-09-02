# This example tells that when calling a method that the subclass
# doesn't implement, python will trace the method down to its 
# parent class.
class A:
	def hello(self):
		print "Hello World"

class B(A):
	pass

# overide the constructor. Even the magic method could be overriden.
class Bird:
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print "Ahhhh, thanks"
			self.hungry = False
		else:
			print "No, thanks" 

#self instance is bounded to object(bound method)
#putting any "self" of class object into __init__ is ok, that is not bound method.
class SongBird(Bird):
	def __init__(self):
		# here __init__ method does not invoke the
		# the super __init__ method. 
		# Object doesn't have hungry property.
		#Bird.__init__(self)
		#super(SongBird, self).__init__()
		self.sound = 'Squawk'
		
	def sing(self):
		print self.sound

# Bird2 inherits object which makes it a new-style class. type Bird2 is type
#class Bird2(object):

__metaclass__ = type
class Bird2():
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print 'Aaaah...'
			self.hungry = False
		else:
			print 'No, thanks!'
class SongBird2(Bird2):
	def __init__(self):
		# here SongBird2(the first argument) must be 
		# a type value. But old-style classes are not type but classobj
		super(SongBird2, self).__init__()
		#super is smart enough to deal with multiple inheritance.
		self.sound = 'Squawk!'
	def sing(self):
		print self.sound 

#protocal and has no need to implement an interface
