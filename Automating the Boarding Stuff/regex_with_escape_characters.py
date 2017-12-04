#use * to signify that a group within a regular expression can exist one or more times 

import re

regex =  re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())
