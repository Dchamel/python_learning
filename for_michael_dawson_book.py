# Some programs while reading a book of Michael Dawson - Python Programming

# import random
# input('Hello in simple Numeric Game. \n   Press Enter to Start...')
# print('\nNow you need try to find out what is My number')
# rand_number = random.randint(1,100)
# print('My number is:', end=' ')
# guess = 0
# while not guess:
#     guess = int(input())
# tries = 1
#
# while guess != rand_number:
#     if guess > rand_number:
#         print('My number is Less')
#     else:
#         print('My number is Higher')
#     guess = int(input('My number: '))
#     tries += 1
#
# print('You Right ! Number of your Tries is: ', tries)
#

# word = input('Enter the Word: ')
# print('All letters of this word: ')
# for n in word:
#     print(n.capitalize(), end=' ')

# import random
# word = 'панк рок цой жиф хой'
# uplen = len(word)
# downlen = -len(word)
# for i in range(40):
#     position = random.randrange(downlen, uplen)
#     if word[position] != ' ':
#         print('Random Letter from the String position number', position, 'is -', word[position])
#     else: continue

# message = input('Input string: ')
# VOWELS = 'aeiouyаеёиоуыя'
# new_message = ''
# for i in message:
#     if i.lower() not in VOWELS:
#         new_message += i
#         print('New string is: ', new_message)
# print('There is new string without VOWELS: ', new_message)

# word = 'NowohoDonozer'
# start = None
# while not start:
#     start = input('Start position: ')
#     if start:
#         start = int(start)
#         end = int(input('End position: '))
#         print(word[start:end])
#     else: break

# inventory = ()
# if not inventory:
#     print('You are','naked'.upper())
# input('Press Enter to Continue')
# inventory = ('sword','shield','armor','healing potion')
# print('Inventory: ')
# for item in inventory:
#     print(item)
# print ('In your Inventory',len(inventory),'items')
# if 'sword' in inventory:
#     print('All Ok :)')
#
# for item in inventory[2:4]:
#     print(item, end=' ')
#
# input('\nPress Enter for Exit')

# import random
# WORDS = ('Hamster','Linux','Gubilet','Sonar','World')
# word_chosen = random.choice(WORDS).lower()
# print(word_chosen)
# crypt_word = ''
# word = word_chosen
# while word:
#     position = random.randrange(len(word))
#     crypt_word += word[position]
#     word = word[:position] + word[(position+1):]
# print(crypt_word)
#
# print('Hi, User')
# user_word = input('Input true word: ').lower()
# while user_word != word_chosen or user_word == "":
#     user_word = input('Try again: ').lower()
# print('Correct !')

# number = int(input('Input number: '))
# step = int(input('Step: '))
# for i in range(0,number,step):
#     print (i)

# inventory = ['shield','sword','armory','healing potion']
# print('Inventory contains: ')
# for item in inventory:
#     print(item)
# input('Press Enter to Continue...')
# print('In your Inventory',len(inventory),'items')
#
# # index = int(input('Enter Index of your Item: '))-1
# # print(inventory[index])
# #
# # start = int(input('Start position of Inventory: '))
# # end = int(input('End position of Inventory: '))
# # print('This part of your Inventory contains: ')
# # print(inventory[start:end])
#
# chest = ['fish','neckless']
# print(chest)
# inventory += chest
# print (inventory)
#
# print('Changing Sword to Bow...')
# inventory[1] = 'Bow'
# print(inventory)
#
# inventory[2:4] = ['Staff']
# print(inventory)
# del inventory[3]
# print(inventory)
# del inventory[:2]
# print(inventory)

# # Page 142


# scores = []
# choise = None
#
# while choise != '0':
#     print(
#     '''
#     0 - Exit
#     1 - Show All records
#     2 - Show Top 5 records
#     3 - Add record
#     4 - Del Record
#     5 - Sort all
#     '''
#     )
#     choise = input('What you want to do: ')
#     if choise == '0':
#         print('See you later')
#     elif choise == '1':
#         print('All Records:')
#         print('Name \t Score')
#         for record in scores:
#             score, name = record
#             print(name,'\t',score)
#     elif choise == '2':
#         print('Top 5 Scores:')
#         for record in scores[:5]:
#             score, name = record
#             print(name,'\t',score)
#     elif choise == '3':
#         name = input("Enter Name of the Player: ")
#         score = int(input("Input Score: "))
#         record = (score, name)
#         scores.append(record)
#     # still dont know how to del element of cell in list
#     # elif choise =='4':
#     #     score = int(input('Which record do you want to DEL: '))
#     #     if score in scores:
#     #         scores.remove(score)
#     #     else: print('I cant find right score')
#     elif choise == '5':
#          scores.sort(reverse=True)
#     else: print('Wrong Input:', choise)

# # Pages 152-159
# voc_codes = {
#     '404': 'Page not found',
#     '502': 'Bad Gateway',
#     '200': 'OK',
#     '202': 'Accepted',
#     '301': 'Moved Permanently',
#     '302': 'Moved Temporarily',
#     '000': 'Prepare for unforeseen consequences...'
# }
# # # Two types of request to the voc_codes
# # if '404' in voc_codes: print(voc_codes['404'])
# # else: print('Wrong Code !')
# # This is much faster
#
# choise = None
# while choise != '0':
#     print(
#         '''
#         Menu:
#
#         0 - Exit
#         1 - Find Code explanation
#         2 - Add Code
#         3 - Change Explanation of Code
#         4 - Delete Code
#         '''
#     )
#     choise = input('What to do: ')
#     # exit
#     if choise == '0':
#         print('End of Prog.')
#
#     # CRUD ops with voc
#     # read
#     elif choise == '1':
#         user_code_read = input('Input ХХХ Code or 0 for Previous Menu: ')
#         voc_answer = ''
#         while user_code_read != '0' or voc_answer == 'Wrong Code !':
#             voc_answer = voc_codes.get(user_code_read, 'Wrong Code !')
#             print(voc_answer)
#             voc_answer = ''
#             user_code_read = input('Input ХХХ Code: ')
#     # create
#     elif choise == '2':
#         user_code_add = input('Input New ХХХ Code: ')
#         if user_code_add not in voc_codes:
#             user_descr_add = input('Enter description for the Code: ')
#             voc_codes[user_code_add] = user_descr_add
#             print('Code', user_code_add, 'added to the vault.')
#         else:
#             print('Code', user_code_add, 'already exists.')
#     # update
#     elif choise == '3':
#         user_code_upd = input('Input XXX Code for update: ')
#         if user_code_upd in voc_codes:
#             user_descr_upd = input('Input New description for the Code: ')
#             voc_codes[user_code_upd] = user_descr_upd
#             print('Description Update complete.')
#         else:
#             print('There is no Code', user_code_upd, 'at the Database.')
#     # delete
#     elif choise == '4':
#         user_code_del = input('Enter the Code for Delete: ')
#         if user_code_del in voc_codes:
#             del voc_codes[user_code_del]
#             print('Code', user_code_del, 'was Deleted from the Database.')
#         else:
#             print('There is no Code', user_code_del, 'at the Database.')
#     else:
#         print('Wrong Input !')
#         input('Press Enter for Exit.')
#

# Page 159- 164
# hangman game
# import random
# HANGMAN = (
# '''
#  ------
#  |    |
#  |
#  |
#  |
#  |
#  |
#  |
#  |
# ----------
# ''',
# '''
#  ------
#  |    |
#  |    O
#  |
#  |
#  |
#  |
#  |
#  |
# ----------
# ''',
# '''
#  ------
#  |    |
#  |    O
#  |   -+-
#  |
#  |
#  |
#  |
#  |
# ----------
# ''',
# '''
#  ------
#  |    |
#  |    O
#  |  /-+-
#  |
#  |
#  |
#  |
#  |
# ----------
# ''',
# '''
#  ------
#  |    |
#  |    O
#  |  /-+-/
#  |
#  |
#  |
#  |
#  |
# ----------
# ''',
# '''
#  ------
#  |    |
#  |    O
#  |  /-+-/
#  |    |
#  |
#  |
#  |
#  |
# ----------
# ''',
# '''
#  ------
#  |    |
#  |    O
#  |  /-+-/
#  |    |
#  |    |
#  |   |
#  |   |
#  |
# ----------
# ''',
# '''
#  ------
#  |    |
#  |    O
#  |  /-+-/
#  |    |
#  |    |
#  |   | |
#  |   | |
#  |
# ----------
# ''')
# FAIL = len(HANGMAN) - 1
# WORDS = ('ubuntu', 'keyboard', 'microcontroller', 'pcb', 'sql')
# word = random.choice(WORDS)
# hidden_word = '#' * len(word)
# mistakes = 0
# user_used_letters = []
#
# # Gameplay
# while mistakes < FAIL and hidden_word != word:
#     print(HANGMAN[mistakes])
#     print('You already checked letters: \n', user_used_letters)
#     print('\n Your current Word looks like: ', hidden_word)
#
#     # Letter Input check for repeat and store
#     user_letter = input('Enter Letter: ')
#     user_letter = user_letter.lower()
#     while user_letter in user_used_letters:
#         print('You used this letter before')
#         user_letter = input('Enter another Letter: ')
#         user_letter = user_letter.lower()
#     user_used_letters.append(user_letter)
#
#     # Letter check for contain in word
#     if user_letter in word:
#         print('Congrats ! Letter', user_letter, 'is in this Word.')
#         new = ''
#         for i in range(len(word)):
#             if user_letter == word[i]:
#                 new += user_letter
#             else:
#                 new += hidden_word[i]
#         hidden_word = new
#     else:
#         print('There is no letter', user_letter, 'in this word.')
#         mistakes += 1
#
# # END OF GAME
# if mistakes == FAIL:
#     print(HANGMAN[mistakes])
#     print('You were Hanged')
# else:
#     print('You have done ! Congrats !')
# input('Press Enter for Exit')

# Page 164 tasks
# Task 1

# import random
# words = ['Life', 'kovid', 'Price', 'trance', 'yellow', 'headphones']

# long ver the same
# user_word_list = []
# for _ in range(len(words)):
#     chosen_word_index = random.randint(0, len(words)-1)
#     user_word_list.append(words[chosen_word_index])
#     del words[chosen_word_index]
# print(user_word_list)

# shorter the same
# for _ in range(len(words)):
#     i = random.choice(words)
#     print(i)
#     words.remove(i)

# the same with while
# while words:
#     i = random.choice(words)
#     print(i)
#     words.remove(i)

# Character points selector for the RPG
# Here i decided to filter Input and i found in Google some new things
# for the exception handling. There is no this 'Try-Except' construction
# before Page 164 and Functions too, but it`s does not matter
# Google is not forbidden while you reading books ;)
# P.S. don`t throw cats in me because of missing ValueError
# I just don`t know what the point in this yet
points = 30
atributes = [['Strength',0],['Health',0],['Withdom',0],['Agility',0]]
def getatribs():
    print('Your free points:',points)
    print('1.',atributes[0][0],' - ',atributes[0][1])
    print('2.',atributes[1][0],' - ',atributes[1][1])
    print('3.',atributes[2][0],' - ',atributes[2][1])
    print('4.',atributes[3][0],' - ',atributes[3][1])
getatribs()
chosen_atr = ''
while chosen_atr != 0:
    try: chosen_atr = int(input('Input number of what do you want to chose or 0 for exit: '))
    except: continue
    if chosen_atr == 0:
        break
    while True:
        try: points_added = int(input('How many Points do you want to spent: '))
        except: continue
        break
    atributes[chosen_atr-1][1] = points_added
    points -= points_added
    getatribs()
