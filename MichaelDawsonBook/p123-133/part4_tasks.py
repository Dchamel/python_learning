# task1
begin = 14
end = 67
step = 3
for i in range(begin,end,step):
    print(i,' ', end='')
print('')

# task2
userWord = 'Commit'
j = len(userWord)
for i in range(j):
    print(userWord[-i-1], end='')
print('')

# task3
import random
WORDS = ('assistance', 'enthusiasm', 'nature',
         'insect', 'assignment', 'road',
         'studio', 'tongue', 'boyfriend', 'movie')
word = random.choice(WORDS)
correct = word
jumble = ''
attempts = 0
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print(jumble)
guess = input('What is this Word ? Answer: ')
while guess != correct:
    print('Sorry. You`re wrong.')
    cheats = input('Do you need a hint ? (y/n) - ')
    if cheats == 'y':
        attempts += 1
        print(f'Some letters of the Correct word "{jumble}" from the beginning -',correct[:attempts])
        guess = input('What is this Word ? Answer: ')
    else:
        guess = input('What is this Word ? Answer: ')
print('Correct !')

# task4
WORDS = ('nature', 'insect', 'road', 'studio',
         'tongue', 'boyfriend', 'movie')
tries = 5
letter = ''
word = random.choice(WORDS)
print(f'This word have {len(word)} letters - {"*"*len(word)}')
while not letter:
    letter = input(f'Input letter from this word. You have {tries} tries - ')
tries -= 1
while tries > 0:
    if letter in word:
        n = word.find(letter)
        j = len(word)
        print(f'Yes - {"*"*n}{letter}{"*"*(j-n-1)} ')
    else:
        print('No letter like this one.')
    letter = ''
    while not letter:
        letter = input(f'Input letter from this word. You have {tries} tries - ')
    tries -= 1

attempts = 3
guess = ''
while not guess: guess = input(f'What is this Word ? You have {attempts} attempts. Answer: ')
while guess != word and attempts > 1:
    print('Sorry. You`re wrong.')
    guess = ''
    attempts -= 1
    while not guess: guess = input(f'What is this Word ? You have {attempts} attempts. Answer: ')
if attempts <= 1:
    print('You`re loose')
else:
    print('Correct !')