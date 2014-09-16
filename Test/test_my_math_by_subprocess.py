import unittest, my_math
from subprocess import Popen, PIPE
class ProductTestCase(unittest.TestCase):
	def testWithPyLint(self):
		cmd = 'pylint', '-rn', 'my_math'
		pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
		self.assertEqual(pylint.stdout.read(), '')
if __name__ == "__main__": unittest.main()
