file = open('1.txt', 'w')
file.write('Hello, File !')
file.close()

file = open('1.txt', 'r')
print(file.read())
file.close()

with open('1.txt', 'a') as file:
    file.write('\nAnother string')
    # print(file.read())!

try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print('You cant devide by Zero')