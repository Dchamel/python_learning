import random

# p112
word = 'Samochod'
print(word[0])
high = len(word)
low = -len(word)
print(high, low)
for i in range(10):
    position = random.randrange(low, high)
    print('word[',position,']\t',word[position])

# word[1] = 'G' # Will be an error

# p117
word = 'Flamenco'
VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
new_message1 = ''
new_message2 = ''
for letter in word:
    if letter.lower() not in VOWELS:
        new_message1 += letter
    elif letter.lower() not in CONSONANTS:
        new_message2 += letter*2
    else:
        print('No Way !')
print(new_message1)
print(new_message2)

# p120
word = 'pizza'
start = None
while start != '':
    start = input('Input Start position: ')
    if start:
        start = int(start)
        finish = int(input('Input Finish position: '))
        print('New word will be -',word[start:finish])

print(word[:2])
print(word[3:])
