#Test is to make code do something and see how it works.
#Change has its danger. If program is well designed, then the effect of
#change should be local and debugging is easier if you spot the bug.

#The 1-2-3(and 4) of Testing
#1.Figure out what the new feature is.
#2.Write skeleton code and make the tests fail.
#3.Write dummpy code.Just to pass the test.
#4.Rewrite the code.

#Tools for testing.

#two standard modules that helps
#doctest: searches for peices of text that look like interactive Python 
#sessions and then executes those sessions.
def square(x):
	'''
	Squares a number and returns the result.
	>>> square(2)
	4
	>>> square(3)
	9
	>>> square(-1)
	1
	'''
	return x*x

if __name__ == '__main__':
	# import doctest and itself.
	import doctest, my_math
	# run the testcase from the doc text
	doctest.testmod(my_math)
#run python my_math.py -v (verbose)
#But what if the  result can not be represented by simple text?  

#unitest: based on JUnit
class ProductTestCase(unittest.TestCase):
	def testIntegers(self):
		for x in range(-10, 10):
			for y in range(-10, 10):
				p = my_math.product(x, y)
				self.failUnless(p == x*y, 'Integer multiplication failed')
	def testFloats(self):
		for x in range(-10, 10):
			for y in range(-10, 10):
				x = x / 10.0
				y = y / 10.0
				p = my_math.product(x, y)
				self.failUnless(p == x*y, 'Float multiplication failed')

if __name__ == "__main__": unittest.main()

#PyChecker and PyLint(used in command-line as subprocess)

#Profile
import profile
from my_math import product
profile.run('product(1,2)')
