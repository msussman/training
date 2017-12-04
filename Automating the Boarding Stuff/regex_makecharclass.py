#make your own character class using re.compile([])

import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowel_list = vowelRegex.findall('Robocop eats baby food')
print(vowel_list)

#match only when there are two vowels in a row

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
vowel_list = vowelRegex.findall('Robocop eats baby food')
print(vowel_list)

#add a ^ to create a negative character class

vowelRegex = re.compile(r'[^aeiouAEIOU]')
vowel_list = vowelRegex.findall('Robocop eats baby food')
print(vowel_list)

