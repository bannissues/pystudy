age = int(input('how many years do you have? '))

if age <= 17:
    print('you are a teenager')
elif 18 >= age <= 23:
    print('you are an young adult!')
elif 24 >= age <= 40:
    print('you\'re an adult!')
elif 41 >= age <= 65:
    print('you are not a fossil (YET)')
else:
    print('you\'re a minor')