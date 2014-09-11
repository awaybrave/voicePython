#Screen Scrapping: scrap the content of websites
from urllib import urlopen
import re, pdb

#grap the anchor information
p = re.compile('<a .*? href="(.*?)>(.*?)</a>')
text = urlopen('http://www.baidu.com').read()
#findall return all the capcture groups and return tuples.
for url, name in p.findall(text):
	print '%s (%s)' % (name, url)

# tidy library correct the messy html makeup file
from subprocess import Popen, PIPE

text = open('messy.html').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)

tidy.stdin.write(text)
tidy.stdin.close()

print tidy.stdout.read()
#note to choose the correct file encoding.

# HTMLParser provides several handlers such as handle_starttag, handle_text
# and handle_endtag for user to deal with tags when parsing the html text.  
from urllib import urlopen
from HTMLParser import HTMLParser
class Scraper(HTMLParser):
	# these two properties work like locks.
	in_h3 = False
	in_link = False

	def handle_starttag(self, tag, attrs):
		attrs = dict(attrs)
		if tag == 'h3':
			self.in_h3 = True

		if tag == 'a' and 'href' in attrs:
			self.in_link = True
			self.chunks = []
			self.url = attrs['href']

	def handle_data(self, data):
		if self.in_link:
			self.chunks.append(data)
	
	def handle_endtag(self, tag):
		if tag == 'h3':
			self.in_h3 = False
		if tag == 'a': 
			if self.in_h3 and self.in_link:
				print '%s (%s)' % (''.join(self.chunks), self.url)
			self.in_link = False

text = urlopen('http://python.org/community/jobs').read()
parser = Scraper()
parser.feed(text)
parser.close()
# I made a mistake here: I named this example HTMLParser.py, then when
# importing the HTMLParser module, then python interpreter looks for this 
# file in the current directory.... Then it caused the infinite loop but
# python import modules once, so it raises the ImportError.
from urllib import urlopen
from HTMLParser import HTMLParser
