from logging import error

hours = int(input('hello, what time is it?\n'))

if 6 <= hours < 12:
    print('oh, thanks, good morning!')
elif 12 >= hours < 18:
    print('thank you, good afternoon!')
elif hours >= 18:
    print('ok, good night!')
elif hours < 6:
    print('you\'re talking to a spirit pal take a nap')
else:
    print('ok this is not supposed to happen')
