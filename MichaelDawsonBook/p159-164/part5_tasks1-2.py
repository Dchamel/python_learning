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
choice = None

print ('\n========================= Welcome ! =========================')

showPlayerCharacteristics = f'''Player stats for now:
Strength: {characteristics['strength']}
Health: {characteristics['health']}
Wisdom: {characteristics['wisdom']}
Agility: {characteristics['agility']}
'''

mainMenu = f'''
{showPlayerCharacteristics}
--- MENU ---
0 - Exit
1 - Change Attributes
2 - Clear All
'''

showMenuChange = f"""
--- MENU ---
0 - Previous Menu
1 - Add Points
2 - Remove Points
"""

changeCharMenu = f'''
--- Change characteristics of the Player ---

{showPlayerCharacteristics}
--- MENU ---
0 - Previous Menu
1 - Change Strength
2 - Change Health
3 - Change Wisdom
4 - Change Agility

\nYou have {points} free Points
'''

def changeAttrMenu(choiceChange):
    t = "Now "
    if choiceChange == '1':
        t += 'Strength is - ' + str(characteristics['strength'])
    elif choiceChange == '2':
        t += 'Health is - ' + str(characteristics['health'])
    elif choiceChange == '3':
        t += 'Wisdom is - ' + str(characteristics['wisdom'])
    else:
        t += 'Agility is - ' + str(characteristics['agility'])
    t += f"""
    \nYou have {points} free Points
    {showMenuChange}
    """
    print(t)
    return

def changeAttr(choiceChange):
    choiceChangeAttr = None
    global points
    global characteristics
    while choiceChangeAttr != '0':
        print(changeAttrMenu(choiceChange))
        choiceChangeAttr = input('Enter: ')
        # Add Points
        if choiceChangeAttr == '1':
            userInputPoints = int(input('How many points you want to add ?'))
            if userInputPoints <= points:
                characteristics['strength'] = userInputPoints
                points -= userInputPoints
            else:
                print(f'You don`t have {userInputPoints} points. Max is - {points}')
        # Remove Points
        elif choiceChangeAttr == '2':
            print('hi')
        elif choiceChangeAttr == '0':
            break
        else:
            print('Wrong choice !')

while choice != '0':
    print(mainMenu)
    choice = input('Enter: ')
    print()

    if choice == '0':
        print('Bye')

    # Change Attributes
    elif choice == '1':
        choiceChange = None
        while choiceChange != '0':
            print(textwrap.dedent(changeCharMenu))
            choiceChange = input('Enter: ')
            print()
            # Change Strength
            if choiceChange == '1':
                changeAttrMenu(choiceChange)
                changeAttr(choiceChange)
            elif choiceChange == '2':
                print(f"Now Health is - {characteristics['health']}")
            elif choiceChange == '3':
                print(f"Now Wisdom is - {characteristics['wisdom']}")
            elif choiceChange == '4':
                print(f"Now Agility is - {characteristics['agility']}")
            elif choiceChange == '0':
                break
            else:
                print('Wrong choice !')

    elif choice == '2':
        characteristics = {'strength': 0, 'health': 0, 'wisdom': 0, 'agility': 0}
        points = 30
    else:
        print('Wrong choice !')



