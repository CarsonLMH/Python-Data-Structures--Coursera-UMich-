import urllib
from BeautifulSoup import *

urlx = 'http://python-data.dr-chuck.net/known_by_Kalia.html'

def name_pos (link, position):
    url = str(link)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    lst = []

    # Retrieve all of the anchor tags
    for tag in tags:
        lst.append(str(tag.get('href', None)))

    yield str(lst[position - 1])

def listloop (link, position, count):
    templink = link
    print 'Starting with: ', templink
    for num in range(count):
        for item in name_pos(templink, 18):
            templink = item
            print 'Iteration ',num+1,': ', templink

listloop(urlx, 18, 7)
