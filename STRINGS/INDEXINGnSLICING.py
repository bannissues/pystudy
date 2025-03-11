from operator import index

phrase = "  anna vitoria is the hottest girl alive"

# indexing and slicing

print(phrase[0]) # the print will be "a" from -a-nna
print(phrase[0:4])
print(phrase[5:12])
print(phrase[-1])

# common methods for strings

print(phrase.upper()) # put the string in uppercase
print(phrase.strip()) #remove unnecessary spaces on the start
print(phrase.replace('hottest', 'cutest'))