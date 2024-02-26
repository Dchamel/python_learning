# Multiple assignment
a, *b, c = [True, 3, 'Flame', 'False', None, 4.5]
print(a, b, c)

# ---------------------------------------------------
a, *b, c = 'Bright Flame'
print(a, b, c)

# ---------------------------------------------------
a, *b, c = 2, 3
print(a, b, c)

s = [4, 10]
print(list(range(1, 5)))
print(list(range(*s)))


# ---------------------------------------------------
def f(a, b, c, d):
    print(a, b, c, d)


f(1, 2, 3, 4)

a = ('hi', 13, True, [1, 'q', 4.5])
f(*a)


# args only for unnamed arguments
# ---------------------------------------------------
def f(*args):
    s = 0
    for i in args:
        s += i
    print(s, args, type(args))


f(1, 2, 3, 4, 5, 6)
f(1, 2)
f(1)


# kwargs only for named arguments
# ---------------------------------------------------
def f(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


f(a=1, b=2, c=3)


# ---------------------------------------------------
def f(*args, **kwargs):
    print(args, kwargs)


f(1, 2, 3, a=22, b=33)
f(101, a=22)


# ---------------------------------------------------
def our_print(*args, sep='#', end='@'):
    print(args, sep, end)


our_print(1, 2)
our_print(1, 2, 3, 4, 5, sep=90)
