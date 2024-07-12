from time import perf_counter

t1 = perf_counter()


# ------BOF------


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

# task 5 - palindrome
# def recurs_factor5(n: str) -> bool:
#     """Takes string and return True if str is a Palindrome"""
#     if n[0] == n[-1]:
#         n = n[1:-1]
#     else:
#         return False
#     if len(n) in [0, 1]:
#         return True
#
#     return recurs_factor5(n)
#
#
# print(recurs_factor5('aabcbaa'))

# task 6 - palindrome without whitespaces
# def recurs_factor6(n: str) -> bool:
#     """Takes palindrome str with whitespaces and return True if str is a Palindrome"""
#     if n[0] != ' ':
#         if n[-1] != ' ':
#             if n[0] == n[-1]:
#                 n = n[1:-1]
#             else:
#                 return False
#             if len(n) in [0, 1]:
#                 return True
#         else:
#             n = n[:-1]
#
#         return recurs_factor6(n)
#     else:
#         return recurs_factor6(n[1:])
#
#
# print(recurs_factor6('ab     a'))
# print(recurs_factor6('a a  ba'))
# print(recurs_factor6('a z a a'))


# task 7 - del vowels from a string
# def recurs_factor7(n: str) -> str:
#     """Takes a str, deleting all vowels from it and return this string without vowels"""
#     VOWELS = ['a', 'e', 'i', 'o', 'u']
#     for letter in n:
#         if letter in VOWELS:
#             return recurs_factor7(n.replace(letter, ''))
#     return n
#
#
# print(recurs_factor7('apple'))
# print(recurs_factor7('pineapple'))


# task 8 - double letters
# def recurs_factor8(n: str) -> str:
#     """Takes a str, doubles each letter in it and return this new str"""
#     if not n:
#         return n
#     return n[0] * 2 + recurs_factor8(n[1:])
#
#
# print(recurs_factor8('apple'))
# print(recurs_factor8('peach'))

# task 8.1 from Ann ^_^
# Merge all elements in one string by Recursion
# list_data = ['a', ['b', 'c', 'd'], ['e', 'f', ['g', ['j', 'k']]]]
# final_str = ''
#
#
# def recurs_81(list_data: list[str, [list]]) -> str:
#     """
#     Recursion. Takes list of lists or strings, get all
#     string elements from it and merge it to one string
#     Use Global final_str: str --- !!!!
#     """
#     global final_str
#     for each in list_data:
#         if type(each) == str:
#             final_str += each
#         else:
#             recurs_81(each)
#     return final_str
#
#
# recurs_81(list_data)
# print(final_str)


# task 8.2 from Ann ^_^
# Square all elements of the list
# list_data = [1, [2, 7, 8], [3, 4], [5, [6, 7]]]
#
#
# def recurs_82(list_data: list[int | list]) -> list[int | list]:
#     """
#     Recursion. Takes elements of the list one by one and Square them.
#     """
#     for i, each in enumerate(list_data):
#         if type(each) == int:
#             list_data[i] = list_data[i] ** 2
#         else:
#             recurs_82(each)
#
#     return list_data
#
#
# print(recurs_82(list_data))

# task 9 - Pascal triangle
def recurs_factor9(n: int) -> str:
    """111"""


print(recurs_factor9('apple'))

# ------EOF------
t2 = perf_counter()
print(f'Working time: {t2 - t1:.2f}')
