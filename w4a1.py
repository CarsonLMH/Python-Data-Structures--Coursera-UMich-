import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_331086.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
num = 0

for tag in tags:
    num += int(tag.contents[0])
    # Look at the the number in the <span> tag
    print 'Contents:',tag.contents[0]

print 'Sum:', num
