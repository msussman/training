#verbose mode - white space does not reflect the actual regular expression

import re

#can also add comments in the regular expression

re.compile(r'''
\d\d\d    # area code
-         # first dash
\d\d\d    # first 3 digits
-         # second dash
\d\d\d\d  # last 4 digits
''', re.VERBOSE)

# in order to use more than one option for second parameter in compile function use the pipe
re.compile(r'''
\d\d\d    # area code
-         # first dash
\d\d\d    # first 3 digits
-         # second dash
\d\d\d\d  # last 4 digits
''', re.VERBOSE | re.IGNORECASE | re.DOTALL)

