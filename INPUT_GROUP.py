# in case of multiple variables in only one input:
data = input('say your name, age and height: ').split()
name = data[0]
age = data[1]
height = data[2]

print(f'i am {name.upper()}, i have {age} years old and {height} centimeters of height                              ')