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
print ('\n========================= Welcome ! =========================')

print(f'''Your Characteristics is:
Strength: {characteristics['strength']}
Health: {characteristics['health']}
Wisdom: {characteristics['wisdom']}
Agility: {characteristics['agility']}
''')
choice = '0'
while choice != '0':
    print('''What do you want to do?
    0 - Exit
    1 - Change characteristics
    2 - Reset characteristics
    ''')