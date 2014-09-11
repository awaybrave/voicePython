import sys 
import _palindrome

string = sys.stdin.read() 
if _palindrome.is_palindrome(string[0:-1]):
	print 'Oh! It is a palindrome!'
else:
	print 'Sorry. It is not a palindrome'
