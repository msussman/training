#use {int} to signify that a group within a regular expression must exist int times 

import re

regex =  re.compile(r'(Ha){3}')
mo = regex.search('I laughed so hard, HaHaHa')
print(mo.group())

#can also match to a range of iterations

regex =  re.compile(r'(Ha){3,5}')
mo = regex.search('I laughed so hard, HaHaHaHa')
print(mo.group())
