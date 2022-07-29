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

q = 5
def someFunc():
    global q
    q += 1
    i = q * 2
    j = q / 2
    k = q // 2
    return i, j, k

someFunc()
print(q)
e, r, k = someFunc()
print(e, r, k)
t = someFunc()
print(type(t))
#If function returns two (or more) variables and it writes
# in one variable it will be a Tuple

q = None
w = ''
e = 0
# q,w,e will be false for if
r = '1'
# but r - not, Don`t forget it.
if (r):
    print('true')

def userInput(text):
    userInput = ''
    while userInput not in ('y','n','yes','no'):
        userInput = input(text).lower()
    return userInput

answer = userInput('Yes(y) or No(n): ')
print(f'Thanks for answering - {answer}')