# Simple tasks from one of the interviews

# Inheritance in OOP
class A1:
    def func1(self):
        print('1')

class B1:
    def func2(self):
        print('2')

class A(A1):
    def func3(self):
        print('3')

class B(B1):
    def func4(self):
        print('4')

class C (A, B):
    def func5(self):
        print('5')


c = C()
c.func5()