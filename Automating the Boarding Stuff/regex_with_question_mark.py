#use ? to signify that a group within a regular expression can exist zero or 1 times 

import re

message = 'The Adventures of Batwoman'

BatRegex = re.compile(r'Bat(wo)?man')
mo = BatRegex.search(message)
print(mo.group())


#if you had a phone number without an area code you could use a regex as follows

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234.  Call me tomorrow.')
print(mo.group())
