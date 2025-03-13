name = input('what\'s your name? ')
age = int(input('how old are you? ')) # INT is used to convert a string to an integer
'''
in addiction to the convertion to integers, we can also convert to:
strings - str
boolean - bool
float - float (for decimal numbers)
'''
zipcode = input('where do you live? ')


print(f'welcome {name}, you have {age} years and live in {zipcode}')
print(type(name))
print(type(age))



