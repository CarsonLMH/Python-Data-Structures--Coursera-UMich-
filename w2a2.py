import re

fh = open("/Users/Carson/Desktop/ML/Python/Data Structures/text.txt",'r')
lst = []

for line in fh:
    num = re.findall('([0-9]+)',line)
    for n in num:
        tmp = int(n)
        lst.append(tmp)

print (sum(lst))
