value = float(input('what\'s the price of your buy?\n'))
discount5 = value - (value * 5)//100
discount10 = value - (value * 10)//100
discount20 = value - (value * 20)//100

if value <= 100:
    print(f'you earned a discount of 10% in your buy, so the value of ${value} became ${discount10:.2f}')
elif value >= 200:
    print(f'you earned a discount of 20% in your buy, so the value of ${value} became ${discount20:.2f}')
else:
    print(f'you earned a discount of 5%, so the value of ${value} became ${discount5:.2f}')
