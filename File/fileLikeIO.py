import sys
# file  is treated as stream
#call unix command : cat file.txt | python file.py pipeline
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print 'Wordcount:', wordcount
