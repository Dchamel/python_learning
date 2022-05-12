# p101
import random
number = random.randint(1, 100)
guess = int(input('Input Number: '))
tries = 1
while number != guess:
    if guess < number:
        print('Mine is more')
    else:
        print('Mine is less')
    guess = int(input('Input Number: '))
    tries += 1
print('Correct ! Number of your tries is:', tries)

# p103 - Tasks
# Task1
sur_tup = ('Surprise1','Surprise2','Surprise3','Surprise4','Surprise5')
i = random.randrange(5)
print(sur_tup[i])

# Task2
eagle = 0
tails = 0
for i in range(100):
    y = random.randrange(2)
    if y == 1:
        eagle += 1
    else:
        tails += 1
print('Eagle:',eagle,'Tails:',tails)

# Task3
number = random.randint(1, 100)
guess = int(input('Input Number: ').replace('', '0'))
tries = 1
max_tries = 7
while number != guess and tries <= max_tries-1:
    if guess < number:
        print('Mine is more')
    else:
        print('Mine is less')
    guess = int(input('Input Number: ').replace('','0'))
    tries += 1
if tries >= max_tries:
    print('You Lose. Try again.')
else:
    print('Correct ! Number of your tries is:', tries)
