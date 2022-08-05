#guess the number
import random


def ask_number(question, low, high):
    '''ask user for number in range, return - integer'''
    response = ''
    while response not in range(low, high):
        response = int(input(question))
    return response


low = 1
high = 100
number = random.randint(low, high)
guess = ask_number('Input Number: ', low, high)
tries = 1
max_tries = 7
while number != guess and tries <= max_tries-1:
    if guess < number:
        print('Mine is more')
    else:
        print('Mine is less')
    guess = ask_number('Input Number: ', low, high)
    tries += 1
if tries >= max_tries:
    print('You Lose. Try again.')
else:
    print('Correct ! Number of your tries is:', tries)