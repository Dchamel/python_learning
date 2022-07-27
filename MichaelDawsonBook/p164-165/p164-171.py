# Shows how documentation works for the function
def instructions():
    '''Shows instruction for the player'''

    print('''
    Input the number from 0 to 8. Each number corresponds to the position. 
    
    0 | 1 | 2 
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    ''')

instructions()

# input output for the functions
def fun1(message):
    print(message*2)

def fun2():
    q = 'asd'*3
    return q

def fun3(message):
    '''Definition for the function'''
    while message not in('q','e'):
        message *= 3
    return message

fun1('qwe')
print(fun2())
