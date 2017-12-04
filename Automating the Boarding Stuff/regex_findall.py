#using findall

import re

phoneRegex =  re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
mo = phoneRegex.findall('Phone #1 123-456-7890  Phone#2 789-456-1234')
print(mo)

#with groups returns list of tuples of strings

phoneRegex =  re.compile(r'(\d\d\d)-(\d\d\d\-\d\d\d\d)')
mo = phoneRegex.findall('Phone #1 123-456-7890  Phone#2 789-456-1234')
print(mo)
