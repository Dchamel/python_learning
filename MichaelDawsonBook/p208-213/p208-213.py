import random
#exceptions

try:
    num = float(input('Input number: '))
except ValueError:
    print('Wrong input. Now num is - ',num:=0)
print(num)

#---------------

for value in (None, bool, 'qwe', 1, '$#' ):
    try:
        print(float(value))
    except TypeError:
        print('Only strings and numbers')
    except ValueError:
        print('Only numbers!')

#---------------

try:
    num = float(input('Number: '))
except ValueError as errorText:
    print('Wrong !')
    print(errorText)
else:
    print(f'Your Float number is - {num}')