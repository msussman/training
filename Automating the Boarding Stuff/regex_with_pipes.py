#use pipe delimiter to search for multiple regular expressions 

import re

message = 'Batmobile lost a wheel'

BatRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = BatRegex.search(message)
print(mo.group())
