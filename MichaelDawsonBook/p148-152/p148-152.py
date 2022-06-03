# Scores 2.0
scores = []
choice = None
while choice != '0':
    print('''
    Scores 2.0
    0 - Exit
    1 - Show Scores
    2 - Add record
    ''')
    choice = input('Enter: ')
    print()

    if choice == '0':
        print('Bye')
    elif choice == '1':
        print('Scores')
        print('NAME\tRESULT')
        for item in scores:
            score, name = item
        print(f'{name}\t{score}')
    elif choice == '2':
        name = input('Enter Name: ')
        score = int(input('Enter Score: '))
        entry = (name, score)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print('Wrong choice')
