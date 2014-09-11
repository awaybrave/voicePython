from urllib import urlopen
import re, pdb

#grap the anchor information
p = re.compile('<a .*? href="(.*?)>(.*?)</a>')
text = urlopen('http://www.baidu.com').read()
for url, name in p.findall(text):
	print '%s (%s)' % (name, url)
