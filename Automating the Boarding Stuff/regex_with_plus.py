#use * to signify that a group within a regular expression can exist one or more times 

import re

message = 'The Adventures of Batwoman'

BatRegex = re.compile(r'Bat(wo)+man')
mo = BatRegex.search(message)
print(mo.group())

