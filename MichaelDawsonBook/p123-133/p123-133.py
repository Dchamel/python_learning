# p124 - rpg
import random

inventory = ()
if not inventory:
    print('You`re empty.')
inventory = ('sword',
             'shield',
             'armor',
             'potion')
print(inventory)
for item in inventory:
    print(item)

# p128 - rpg2
inventory = ('sword',
             'shield',
             'armor',
             'potion')
print('You have', len(inventory),'items.')
if 'potion' in inventory:
    print('You`ll be healthy.')
print('By number 2 in your inventory is -', inventory[2])
print('Few items from your Inventory:',inventory[2:4])
chest = ('gold', 'old t-shirt')
inventory += chest
print(inventory)

# p130
WORDS = ('assistance', 'enthusiasm', 'nature',
         'insect', 'assignment', 'road',
         'studio', 'tongue', 'boyfriend', 'movie')
word = random.choice(WORDS)
correct = word
print(word)
jumble = ''
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print(jumble)
guess = input('What is this Word ? Answer: ')
while guess != correct:
    print('Sorry. You`re wrong.')
    guess = input('What is this Word ? Answer: ')
print('Correct !')