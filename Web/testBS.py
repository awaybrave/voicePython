from urllib import urlopen
from bs4 import BeautifulSoup

text = urlopen('https://docs.python.org/2/library/re.html').read()
soup = BeautifulSoup(text)

jobs = set()

for header in soup('li'):
	links = header('a', 'reference') 
	if not links: continue
	link = links[0]
	jobs.add('%s (%s)' % (link.string, link['href']))

print type(header)
print type(links)
print '\n'.join(sorted(jobs, key=lambda s: s.lower())) 
