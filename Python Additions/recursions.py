from time import perf_counter

t1 = perf_counter()

# 20 recursion tasks
# task 1 - factorial
# def recurs_factor(n: int) -> int:
#     if n <= 1:
#         return n
#     else:
#         return n * recurs_factor(n - 1)
#
#
# print(recurs_factor(7))
# print(7 * (6 * (5 * (4 * (3 * (2 * (1)))))))

# task 2 - summ
# Summ from 1 to n
# def recurs_factor2(n: int) -> int:
#     if n <= 1:
#         return n
#     else:
#         return n + recurs_factor2(n - 1)
#
#
# print(recurs_factor2(7))

# task 3 - Summ odd from a list
# def recurs_factor3(n: list[int]) -> int:
#     for i in n:
#         if i % 2 != 0:
#             n.remove(i)
#             if len(n) > 1:
#                 return i + recurs_factor3(n)
#             else:
#                 return i
#         else:
#             if len(n) > 1:
#                 n.remove(i)
#                 return recurs_factor3(n)
#             else:
#                 return 0
#
#
# print(recurs_factor3([1, 2, 3, 4, 5, 6, 7]))
# print(recurs_factor3([1, 2, 4, 6]))


# task 4 - Summ odd from a list
# def recurs_factor4(n: list[int]) -> int:
#     for i in n:
#         if i % 2 != 0:
#             n.remove(i)
#             if len(n) >= 1:
#                 return i + recurs_factor4(n)
#             else:
#                 return i
#         else:
#             n.remove(i)
#             if len(n) >= 1:
#                 return -i + recurs_factor4(n)
#             else:
#                 return -i
#
#
# print(recurs_factor4([1, 2, 3, 4]))
# print(recurs_factor4([1, 2, 3, 4, 5]))

# task 5 - Summ odd from a list
# def recurs_factor4(n: list[int]) -> int:
#     for i in n:
#         if i % 2 != 0:
#             n.remove(i)
#             if len(n) >= 1:
#                 return i + recurs_factor4(n)
#             else:
#                 return i
#         else:
#             n.remove(i)
#             if len(n) >= 1:
#                 return -i + recurs_factor4(n)
#             else:
#                 return -i
#
#
# print(recurs_factor4([1, 2, 3, 4]))
# print(recurs_factor4([1, 2, 3, 4, 5]))


t2 = perf_counter()
print(f'Working time: {t2 - t1:.2f}')