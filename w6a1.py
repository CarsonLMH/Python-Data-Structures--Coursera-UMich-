import urllib
import json

def jsoncount(url):
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved', len(data), 'characters'

    info = json.loads(str(data))
    print 'Count:', len(info["comments"])

    total = 0
    for i in range(len(info["comments"])):
        total += info["comments"][i]["count"]

    print 'Sum:', total

link = 'http://python-data.dr-chuck.net/comments_331087.json'
jsoncount(link)
