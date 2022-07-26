dict = {}

menu1 = """0 - Exit
1 - Add or Edit new Entry
2 - Find Father or Grandfather by son`s name
3 - Show All
4 - Clear All
5 - Del Specified Entry
"""

userInput = ''
while userInput != '0': #Exit
    print(menu1)
    userInput = input('Your choice: ')
    if userInput == '0':
        print('Bye')
        break
    elif userInput == '1': #Add & Edit
        print('Please input names of a Son, Father and a Grandfather below.\nExistent will be overwritten.')
        son = input('Input Son name: ')
        father = input('Input Father name: ')
        grandfather = input('Input Grandfather name: ')
        dict[son] = father, grandfather
    elif userInput == '2': #Find
        print('Input Son`s name to search his Father.')
        userInputSearch = input('Name:')
        print(f'Son name: {userInputSearch}\nFather name: {dict[userInputSearch][0]}\nGrandfather name: {dict[userInputSearch][1]}\n----')
    elif userInput == '3': #Show all
        for s,i in dict.items():
            print(f'Son name: {s}\nFather name: {i[0]}\nGrandfather name: {i[1]}\n----')
    elif userInput == '4': #Del all
        print('All was cleared')
        dict = {}
    elif userInput == '5': #Del 1 Entry
        print('For delete Special Pair Son-Father input Son`s name below')
        userInputDel1Entry = input('Name:')
        del dict[userInputDel1Entry]
    else:
        print('Wrong Input')



