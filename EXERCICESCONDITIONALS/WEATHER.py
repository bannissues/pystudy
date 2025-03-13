weather = int(input('what\'s the temperature of the day? '))

if weather <= 10:
    print(f'the temperature is {weather}C? it\'s a cold day!')
elif weather <=20:
    print(f'oh, it\'s {weather}C outside? it\'s a good time to a walk!')
else:
    print('there is a sun to each one')