#dictionary
codes = {'404':'Not Found',
        '403':'Forbidden',
        '200':'OK',
        '202':'Accepted',
        '301':'Moved Permanently',
        '400':'Bad Request',
        '414':'URI Too Long',
        '418':'I\'m a teapot'
        }
print(codes['404'])
if '403' in codes:
        print(codes['403'])
if '402' in codes:
        print(codes['402'])
#get
print(codes.get('402','There is No Key with number like this one'))

#Codes prog
choice = None
while choice != '0':
        print('''
        0 - Exit
        1 - Find Error by Code
        2 - Add Error
        3 - Change Error in DB
        4 - Delete Error from the DB
        ''')
        choice = input('Enter choice: ')
        print()
        if choice == '0':
                print('Bye')
        elif choice == '1':
                term = input('Enter Code for change it`s Description')
                if term in codes:
                        descr = codes[term]
                        print(f'{term} means "{descr}"')
                else:
                        print('There`s no such code in our DB')
        elif choice == '2':
                term = input('Enter Code for Add')
                if term not in codes:
                        descr = input('Enter Description: ')
                        codes[term] = descr
                        print('Code was added.')
                else:
                        print('This code already in DB')
        elif choice == '3':
                term = input('Enter Code for Change')
                if term in codes:
                        descr = input('Enter Description: ')
                        codes[term] = descr
                        print(f'Code {term} has been changed')
                else:
                        print('There`s no such code in our DB')
        elif choice == '4':
                term = input('Enter Code for Change')
                if term in codes:
                        del codes[term]
                        print('The deletion was completed successfully')
                else:
                        print('There`s no such code in our DB')