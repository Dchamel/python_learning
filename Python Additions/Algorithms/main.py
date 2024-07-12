# # Алгоритм Евклида
# def euclid_algo(a, b):
#     while b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     return a
#
#
# a = 21
# b = 10
# result = euclid_algo(a, b)
# print(result)
#
#
# # Алгоритм Карацубы
# def karacuba(x, y):
#     if x < 10 or y < 10:
#         return x * y
#
#     n = max(len(str(x)), len(str(y)))
#     m = n // 2
#
#     a, b = divmod(x, 10 ** m)
#     c, d = divmod(y, 10 ** m)
#
#     ac = karacuba(a, c)
#     bd = karacuba(b, d)
#
#     ad_bc = karacuba(a + b, c + d) - ac - bd
#
#     res = ac * 10 ** (2 * m) + ad_bc * 10 ** m + bd
#
#     return res
#
#
# x = 2345
# y = 3456
#
# res = karacuba(x, y)
# print(res)

# --------------------------------------------------------------------------
# Алгоритмы поиска

# --------------------------------------------------------------------------
# Алгоритмы сортировки

def selection_sort(array) -> list:
    for i, item1 in enumerate(array):
        for j, item2 in enumerate(array):
            if array[i] > item2:
                array[i], array[j] = array[j], array[i]

    return array


arr = [21, 11, 45, 5, 76, 34, 18, 77]

print(selection_sort(arr))
