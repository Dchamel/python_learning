# p75
import random
ran1 = random.randint(1,6)
ran2 = random.randrange(6)+1
total = ran1 + ran2
print(total)

# p76
login = input('Input Login:')
if login == 'admin':
    print('Hello,', login.title())

# p77
login = input('Login: ')
if login == 'admin':
    print('Hello, Boss')
else:
    print('Access Denied')

# p81
mood = random.randint(1,3)
if mood == 1:
    print('You are happy !')
elif mood == 2:
    print('You`re OK')
elif mood == 3:
    print('You are Sad :(')
else:
    print('It can not be true :o')