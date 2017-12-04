#add ( around groups within a regular expression to be able to parse them out 

import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)
area_code = mo.group(1)
print(area_code)
seven_dig = mo.group(2)
print(seven_dig)
