def summa(a, b, c):
    print(a + b + c)
summa(1, 2, 3)


def summa(*znach):
    print(sum(znach))
summa(1, 2, 3, 4, 5, 6, 7, 8)


def brands(**all):
    print(all)
brands(a='Apple', s='Samsung', v='taz')


def brands(**all):
    for q, w in all.items():
        print(q, ':', w)
brands(a='Apple', s='Samsung', v='taz')