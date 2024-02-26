def decorator(func):
    def inner():
        print('start decorator')
        func()
        print('end decorator')

    return inner


def say():
    print('hello world')


def buy():
    print('buy world')


say = decorator(say)
print(say)
say()

buy = decorator(buy)
buy()


# ---------------------------------------------------

def decorator(func):
    def inner(*args, **kwargs):
        print('start decorator')
        func(*args, **kwargs)
        print('end decorator')

    return inner


def say(name, surname, age):
    print('hello', name, surname, age)


say = decorator(say)
say('Lukas', 'Feinberg', 30)


# funcs before decorator @
# ---------------------------------------------------
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


def say(name, surname, age):
    print('hello', name, surname, age)


say = table(header(say))
say('Lukas', 'Feinberg', 30)


# the same but with @ decorator
# ---------------------------------------------------
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


@table
@header
def say(name, surname, age):
    print('hello', name, surname, age)


say('Lukas', 'Feinberg', 30)


# how to save doc and name of the func
# the first way
# ---------------------------------------------------

def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__

    return inner


def say():
    print('hello world')


def sqr(x):
    '''
    Square of input number
    :param x:
    :return:
    '''
    print(x ** 2)


say = table(say)
say()
print(say.__name__)

print(sqr.__name__)
help(sqr)
sqr = table(sqr)
help(sqr)
sqr(2)

# how to save doc and name of the func
# the second way
# ---------------------------------------------------
from functools import wraps


def table(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


def say():
    print('hello world')


def sqr(x):
    '''
    Square of input number
    :param x:
    :return:
    '''
    print(x ** 2)


say = table(say)
say()
print(say.__name__)

print(sqr.__name__)
help(sqr)
sqr = table(sqr)
help(sqr)
sqr(2)
