
import re

# use . to signfy any character that isn't a \n

atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# * means zero or more, . means anything

string = 'First Name: Al Last Name: Sweigart'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
name_list = nameRegex.findall(string)
print(name_list)
first_name = name_list[0][0]
print(first_name)

# nongreedy matches will include a ? ie. .*?

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
nongreedy_list = nongreedy.findall(serve)
print(nongreedy_list)

# greedy matches 
serve = '<To serve humans> for dinner.>'
greedy = re.compile(r'<(.*)>')
greedy_list = greedy.findall(serve)
print(greedy_list)

# re.DOTALL allows * to include everything including new lines

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotStar = re.compile(r'.*')
print(dotStar.search(prime))
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

#re.I - ignores case

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))

vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))
