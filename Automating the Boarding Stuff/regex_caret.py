
import re

# use ^ to signfy the regular expression must occur a beginning or ends to $

beginswithHelloRegex = re.compile(r'^Hello')
mo = beginswithHelloRegex.search('Hello, why didn\'t you say Hello as well?')
print(mo.group())

endwithWordlRegex =  re.compile(r'world!?')
mo = endwithWordlRegex.search('Hello world!')
print(mo.group())

#use both ^ and $ to signify that regular expression must be the entire text
AllDigitsRegex = re.compile(r'^\d+$')
mo = AllDigitsRegex.search('123r4587')
print(mo.group())
