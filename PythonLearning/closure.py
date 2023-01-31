def main_func(name):
    def inner_function():
        print('hello my friend', name)

    return inner_function


# ---------------------------------------------------
def adder(value):
    def inner(a):
        return value + a

    return inner


# ---------------------------------------------------
def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


# ---------------------------------------------------
def average_numbers():
    summa = 0
    count = 0

    def inner(number):
        nonlocal summa, count
        summa += number
        count += 1
        return summa / count

    return inner


# ---------------------------------------------------
from time import perf_counter


def timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner


# ---------------------------------------------------
def add(a, b):
    return a + b


def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Func {func.__name__} called {count} times')
        return func(*args, **kwargs)

    return inner
