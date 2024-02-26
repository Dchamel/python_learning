from time import perf_counter

t1 = perf_counter()


# At First - factorial. The most popular examle.
# def recurs_factor(n: int) -> int:
#     if n <= 1:
#         return n
#     else:
#         return n * recurs_factor(n - 1)
#
#
# print(recurs_factor(7))


# print(7 * (6 * (5 * (4 * (3 * (2 * (1)))))))

# Summ from 1 to n
# def recurs_factor2(n: int) -> int:
#     if n <= 1:
#         return n
#     else:
#         return n + recurs_factor2(n - 1)
#
#
# print(recurs_factor2(7))

# li = [1, 2, 3, 4]
# for i in li:
#     li.remove(i)
#     print(li)
#
#     break


# Summ odd from a list
def recurs_factor3(n: list[int]) -> int:
    for i in n:
        if i % 2 != 0:
            n.remove(i)
            if len(n) > 1:
                return i + recurs_factor3(n)
            else:
                return i
        else:
            if len(n) > 1:
                n.remove(i)
                return recurs_factor3(n)
            else:
                return 0


print(recurs_factor3([1, 2, 3, 4, 5, 6, 7]))
print(recurs_factor3([1, 2, 4, 6]))

t2 = perf_counter()
print(f'Working time: {t2 - t1:.2f}')
