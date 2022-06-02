inventory = ['sword','shield','armor','healing potion']
print(f'Now you have {inventory}')
if 'healing potion' in inventory:
    print('All be OK')
start = 1
finish = 3
print(f'Cut of the list will be {inventory[start:finish]}')
chest = ['gold','jewels','dagger']
inventory += chest
print(inventory)
inventory[1] = 'bow'
print(inventory)
inventory[2:5] = ['silver rose']
print(inventory)
del inventory[1]
print(inventory)
del inventory[:2]
print(inventory)

# Scores
scores = []
choice = None

while choice != '0':
    print("""
    Main Menu
    0 - Exit
    1 - Show Scores
    2 - Add Score
    3 - Delete Score
    4 - Sort list
    """)
    choice = input('Your Choice: ')
    print()
    if choice == '0':
        print('See ya')
    elif choice == '1':
        print('Scores')
        for score in scores:
            print(score)
    elif choice == '2':
        score = int(input('Enter new Score: '))
        scores.append(score)
    elif choice == '3':
        score = int(input('What Score we should Delete?: '))
        if score in scores:
            scores.remove(score)
        else:
            print('Not Exist')
    elif choice == '4':
        scores.sort(reverse=True)
    else:
        print('Wrong choice')