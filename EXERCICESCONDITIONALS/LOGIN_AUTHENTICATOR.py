user = 'admin'
password = '123456'
user_authenticator = input('hello, please insert your username: ')

if user_authenticator == user:
    password_authenticator = input('now insert your password: ')
    if password_authenticator == password:
        print('welcome, ratão da massa!')
    else:
        print('wrong password, please try again')
else:
    print('wrong username, please try again.')
