import sys

string = sys.stdin.read()
string = string[0:-1]
n = len(string)
for i in range(n):
	if string[i] != string[n-i-1]:
		print 'NO'
		break
print 'Yes'
