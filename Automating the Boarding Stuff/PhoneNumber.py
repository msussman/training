import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(message)
print(mo)
