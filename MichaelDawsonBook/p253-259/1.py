# Simple tasks from one of the interviews

s = 'Кошка'

def polomaka(s):
    s = s.lower()
    s = s[::-1]
    s = list(s)
    s.pop(1)
    s = ''.join(s)
    return s.capitalize()

print(polomaka(s))

# Inheritance in OOP
class A:
    def func(self):
        print('1')

class B(A):
    def func2(self):
        print('2')

b = B()
A.func = B.func2
b.func()