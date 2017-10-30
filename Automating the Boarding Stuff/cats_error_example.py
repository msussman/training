print('How many cats do you have?')
numCats = input()

try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    elif int(numCats)< 0:
        print('Enter a positive number')
    else:
        print('Nice')

except ValueError:
    print('You did not enter a number.')
    
    
