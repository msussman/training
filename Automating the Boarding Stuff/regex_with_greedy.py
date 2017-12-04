#when matching a range in regular expression default is to the longest or greedy match 

import re

regex =  re.compile(r'(\d){3,5}')
mo = regex.search('1234567890')
print(mo.group())

#if you use a ? after the range expression, changes to a non-greedy match

regex =  re.compile(r'(\d){3,5}?')
mo = regex.search('1234567890')
print(mo.group())
