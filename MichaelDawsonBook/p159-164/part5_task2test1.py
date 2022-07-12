# Global and nonlocal

tuple1 = (1,2,3,4)
def first():
    print(tuple1)
first()

a = 10
b = 20
def func():
    global a
    print(a)
    a += 11
    print(a)
func()
print(a)

dict1 = {'q':1, 'w':2, 'e':3}
def func1():
    global dict1
    # print(dict1)
    dict1['q'] += 1
    print(dict1)
func1()
# print(dict1)
i = 0
while i < 3:
    func1()
    i += 1
print()
# nonlocal
dict2 = {'q':1, 'w':2, 'e':3}
def func2():
    dict2['e'] -= 1
    print(dict2)
def func3():
    dict2['w'] += 1
    print(dict2)
    func2()
func3()

print()
dict4 = {'q':1, 'w':2, 'e':3}
def func4():
    dict4['w'] += 1
    print(dict4)
func4()
print(globals()['dict4'])