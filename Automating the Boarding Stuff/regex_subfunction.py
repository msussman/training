#find and replace with regular expression with the sub function

import re

namesRegex = re.compile(r'Agent \w+')
find_names = namesRegex.findall('Agent Alice gave the secret document to Agent Bob')
print(find_names)
sub_names = namesRegex.sub('REDACTED', 'Agent Alice gave the secret document to Agent Bob')
print(sub_names)

#substitute using part of original text - use Agent and first letter of name

namesRegex = re.compile(r'Agent (\w)\w*')
find_names = namesRegex.findall('Agent Alice gave the secret document to Agent Bob')
print(find_names)
sub_names = namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret document to Agent Bob')
print(sub_names)
