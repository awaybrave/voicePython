#import sys and sys.argv contains the arguments passed to Python
#interpreter(including the file name).  

import sys
#sys.argv[0] is the file name of the executed script.
args = sys.argv[1:]
args.reverse()
print args

#unlike sys that contains runtime info, os module contains
#operating system info.

#such as 
import os
print os.environ
print os.linesep
print os.sep # path separator
print os.pathsep # paths separator

# we can use os.sep to do path join under any operarting system.
# linesep is the sysblom. 

#Also we can use os.system('/usr/bin/firefox') to execute a program.

#In the case for opening a browser, we can do it in this way: 
import webbrowser
webbrowser.open("http://www.python.org")

#The fileinput module provide sneak way to deal with files.  
import fileinput                         # 1
                                         # 2
for line in fileinput.input(inplace=True): # 3
	line = line.rstrip()                    # 4
	num = fileinput.lineno()                # 5
	print '%-40s #%2i' % (line, num)        # 6
#fileinput.input may switch the stdout to the file(it can change the 
#content of itself)..

# Other than common data structures like list, tuple, dictionary,
# Python also provides set, heap and deque.

#set provides all the set opertion like difference, union, or and the 
#check of superset and subset(Set stores data in an arbitrary order).

a = set([1,2,3])
b = set([2,3,4])

a.union(b) # --> union set
a & b # interset
a.issubset(b) # Is a the subset of b ? 
a.issuperset(b) # Is a the superset of b?

# set is mutable but set contains hashable value(immutable).

# It we want a set to contains sets, then we should transform
# a set into frozenset.

s1 = set()
s2 = set()
try:
	s2.add(s1)
except:
	s2.add(frozenset(s1))
# heap: python doesn't provide a heap type but heapq module
# provide 6 functions to manipulate list like a heap.

#regular expression:
# re of every language has a concep of wildcard. In python, '.' matches any character except
# the newline character.
import re
re1 = re.compile('.ython' ) #-> re1 matches 'python', 'jyhton', ' ython' ....
#using slash companying the special charactor.  
re2 = re.compile('python\.org') # re2 matches 'python.org'
#using character sets:
re3 = re.compile('[a-zA-Z0-9]')
#or reverset the sets:
re4 = re.compile('[^abc]') #which indicates that the a,b,c characters can't be in the matching strings.
#alternative
re5 = re.compile('p(ython|erl)')
#optional and repeated:
re6 = re.compile(r'(http://)?(www\.)?python\.org') #using raw string to reduce the number of backslashed needed.
# (pattern)*, (pattern)+, (pattern){m, n} 

some_text = 'alpha, beta,,,,gamma,   delta'
splitAr = re.split('[, ]+', some_text) 
# the regular expression may use greedy algorithm to run the simulation.

#There are some other simple examples in re/simpleExampley.py,
#some functions receives flag(optional) which changes how the 
#regular expressions are interpreted.  
#eg.
re.split(' ', some_text, maxsplit=3)

#Groups are enclosed in parentheses in order.

# re.VERBOSE allows regular expression pattern including whitespace
# or tab which could make it more readable and removing those characters
# when compiling it.
empthasis_pattern = re.compile(r'''
	\* 		# Beginning emphasis tag --an asterisk
	( 		# Begin group for capturing phrase
	[^'*]+	# Capture anything except asterisk
	)		# End group
	\*		# Ending emphasis tag
''', re.VERBOSE) 


#Greedy and nongreedy pattern
r'\*(.+)\*' # This is a greedy pattern for + in the first group
			# matches as many characters as it can.
# adding an question mark makes it nongreedy:
r'\*(.+?)\*'
#Using +? instead of +, which means that the pattern will match one or 
#more occurences of the wildcard.

#Example: template system.
field_pat = re.compile(r'\[(.+?)\]')

# create a namespace to hold template variables.
scope = {}

def replacement(match):
	code = match.group(1)
	try:
		return str(eval(code, scope))
	except SyntaxError:
		exec code in scope
		return '' 
lines = []
for line in fileinput.input():
	lines.append(line)
text = ''.join(lines)

# function can be passed as function parameter in python
print field_pat.sub(replacement, text)

#Other standar libaries:
#csv, timeit(for measure program time), profile(measure effciency)
#trace(code coverage)
