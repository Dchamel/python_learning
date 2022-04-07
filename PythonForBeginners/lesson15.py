with open('lesson15.txt', 'r') as file:
    line_num = int(file.readline())
    for i in range(line_num):
        a, b = map(int, file.readline().split())
        print(a+b)

def f(a, b):
    return a * b

a = map(f, [2, 4, 5], [5, 6 ,7])
print(list(a))
a = map(f, [2, 4, 5], [5, 6])
print(list(a))

a = map(lambda x: x+10, (2, 4, 5))
print(list(a))

def f(a):
    if a % 2 == 0:
        return a
a = filter(f, (2,3,4,5,6))
print(list(a))

# because i have to put else after if in lambda func i can finish it with "False" or "0"
a = filter((lambda a: a if a%2==0 else False or 0), (2,3,4,5,6))
print(list(a))

# Reduce

from functools import reduce
print(reduce(lambda a,b: a*b, (2,3,4)))

a = [1,2,3,4,5,6,7]
b = 'qwerty'
res = zip(a, b)
print(list(res))