# The Gallows

import random

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")
MAX_WRONG = len(HANGMAN)-1
WORDS = ('PYTHON','CROWBAR','FREEMAN','ALYX','DOG')
word = random.choice(WORDS)
so_far = '-' * len(word)
wrong = 0
used = []
print('Welcome to the Hangman Game')
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print(f'You already chose this letters - {used}')
    print(f'Word for now - {so_far}')

    guess = input('Input Letter: ')
    guess = guess.upper()
    while guess in used:
        print('You already chosen this letter')
        guess = input('Input Letter: ')
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print(f'This letter ({guess}) exists in the word')
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print(f'You`re wrong. There is no "{guess}" letter in this word')
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print('You`re hanged')
else:
    print('You`re the Winner !')
    print(f'Word - {word} was guessed')