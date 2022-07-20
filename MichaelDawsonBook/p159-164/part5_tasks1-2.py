import inspect
import random

# task1
import textwrap

WORDS = ['sword','crowbar','headcrab','dog','combine','freeman','hole','dog','mesa']
# newWords = list(set(WORDS)) del duplicates
# if one of the elements of the list will be another list
# it calls en Error. Then better way will be to  do this:
def delListDuplicates(lis):
    newList = []
    for i in WORDS:
        if i not in newList:
            newList.append(i)
    return newList
newList = delListDuplicates(WORDS)
random.shuffle(newList)
for i in newList:
    print(i)

# task2
# test for global dictionary
characteristics = {'strength':0,'health':0,'wisdom':0,'agility':0}
points = 30

menu1 = '''What do you want to do?
0 - Exit
1 - Change characteristics
2 - Reset characteristics'''

menu2 = '''What do you want to change ?
1 - Strength
2 - Health
3 - Wisdom
4 - Agility
0 - Back'''

menu3 = '''What do you want to do?
1 - Add points
2 - Del points
0 - Back'''
print ('\n========================= Welcome ! =========================')

print(f'''Your Characteristics is:
Strength: {characteristics['strength']}
Health: {characteristics['health']}
Wisdom: {characteristics['wisdom']}
Agility: {characteristics['agility']}
''')
choice = '0'
while choice == '0':
    print(menu1)
    choice = input('Enter choice: ')
    if choice == '1':
        choice2 = '0'
        print(menu2)
        choice2 = input('Enter choice: ')
        if choice2 == '0':

            break
        elif choice2 == '1':
            choice3 = '0'
            print(menu3)
            choice3 = input('Enter choice: ')
        elif choice2 == '2':
            choice3 = '0'
            print(menu3)
            choice3 = input('Enter choice: ')
        elif choice2 == '3':
            choice3 = '0'
            print(menu3)
            choice3 = input('Enter choice: ')
        elif choice2 == '4':
            choice3 = '0'
            print(menu3)
            choice3 = input('Enter choice: ')
    elif choice == '2':
        characteristics = {'strength':0,'health':0,'wisdom':0,'agility':0}
    elif choice == '0':
        break
    else:
        print('Wrong input.')