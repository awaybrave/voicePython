import re
#1. splitting
some_text = 'alpha, beta,,,,gamma,   delta'
splitArr = re.split('[, ]+', some_text) # greedy algorithm
print splitArr , len(splitArr)
splitArr2 = re.split('[, ]+', some_text, maxsplit=2)
print splitArr2, len(splitArr2)
splitArr3 = re.split('[, ]+', some_text, maxsplit=1)
print splitArr3, len(splitArr3)
pat = '[a-zA-Z]+'

#2.find all
text = 'Hello, my dear, hahah!!!! How are you doing? '
print re.findall(pat, text)

#3.substitute
pat = '{name}' # does {} quote something?
text2 = 'Dear {name}...'
print re.sub(pat, 'Mr, R', text2)

#4.escaping
print re.escape('www.python.org')
print re.escape('But where is the ambiguity?')

