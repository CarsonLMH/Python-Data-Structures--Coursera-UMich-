import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_331083.xml'
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
print 'Num count:', len(lst)
total = 0

for item in lst:
    total += int(item.find('count').text)

print 'Total:', total
