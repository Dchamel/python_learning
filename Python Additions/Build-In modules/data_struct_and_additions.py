# # array
# # similar to lists, but have a limited type
# import array
#
# my_array = array.array('u', 'hello')
# my_array2 = array.array('b', b'is array')
# my_array3 = array.array('l', [1, 2, 3, 4])
# my_array4 = array.array('d', [1, 2])
# my_array5 = array.array('i', [1, 2])
#
# print(my_array, my_array2, my_array3, my_array4, my_array5, sep='\n')
#
# # -----------------------------

# # bisect
# # insert to ordered list
# import bisect
#
# # example1
# ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(bisect.bisect_left(ordered_list, 2))
# print(bisect.bisect_right(ordered_list, 2))
# print(ordered_list)
# print(bisect.insort_left(ordered_list, 2))
# print(ordered_list)
#
#
# # example2
# def grade(score, breakpoints=[30, 40, 50, 60], grades='ABC'):
#     i = bisect(breakpoints, score)
#     return grades[i]
#
#
# print([grade(score) for score in [32, 43, 11, 40, 20, 200]])
#
# # -----------------------------

# # functools
# # Functools module is designed for higher-order functions:
# # functions that act on or return other functions
# from functools import lru_cache
# import requests
#
#
# # Two types of decorators for cache
# # First tpe - lru
# @lru_cache(maxsize=32)
# def get_with_cache(url):
#     try:
#         r = requests.get(url)
#         return r.text
#     except:
#         return "Not Found"
#
#
# for url in ['https://ya.ru/',
#             'https://google.com/',
#             'https://msn.com']:
#     get_with_cache(url)
#
# print(get_with_cache.cache_info())
#
# # Second type - cached property
# from functools import cached_property
#
#
# class Page:
#     @cached_property
#     def render(self, value):
#         # do somth high-load and as fact for showing html-page
#         return html
#
#
# functools have a lot of methods for different cases like
# Automatic implementation of comparison operators
# from functools import total_ordering
# Overloading methods/functions
# from functools import singledispatch
# from functools import singledispatchmethod
# Passing callback functions
# from functools import partial
# Saving the name and documentation lines of the decorator function
# from functools import wraps
# Reduce func - sum items of iter object or somth like that
# from functools import
#
# # -----------------------------

# # heapq
# # Quick and easy way to create any type of priority queue for your application
#
# import heapq
#
# a = [1, 6, 4, 3, 2]
# heapq.heapify(a)
# print('Heap =', a)
# heapq.heappush(a, 10)
# print(a)
# poped_element = heapq.heappop(a)
# print(poped_element)
# #
# # -----------------------------

# copy
# For light and deep copy of object

# import copy

# data = {1: 5, 2: 6, 3: 7, 4: 8, 5: {10: 11}}
# new_data = copy.copy(data)
# data[7] = 99
# data[8] = 101
# data[5][10] = 111
# print(data)
# print(new_data)
#
# new_data_deep = copy.deepcopy(data)
# data[5][10] = 112
# print(new_data_deep)
#
# -----------------------------

# # collections
# # Containers for handy work with data
#
# import collections
#
# first = {'two': 22, 'three': 33, 'four': 44}
# last = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
#
# d = collections.ChainMap(first, last)
# print(d)
#
# # -----------------------------
#
# # itertools
# # Itertools creates iterators and works fast with sufficient use of memory
#
# import itertools
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for list_obj in itertools.repeat(lst, 2):
#     for i in list_obj:
#         print(i)
#
# l1 = list(itertools.accumulate(range(10)))
# print(l1)
#
# lst = ['foo', 'bar', ['baz', 'qux']]
# new_lst = list(itertools.chain(lst, range(5)))
# print(new_lst)
#
# vehicles = [('Ford', 'Taurus'), ('Dodge', 'Business'), ('Ford', 'F150'), ('Chevrolet', 'Cobalt')]
# for key, group in itertools.groupby(vehicles, key=lambda x: x[0]):
#     print(key, list(group))
#
# l2 = list(itertools.combinations('WXYZ', 2))
# print(l2)
#
# # -----------------------------

# traceback
# Traceback interface for extraction and formatting and print stack of programs
# Mimics the behavior of the Python interpreter

import traceback


def another_function():
    lumberstack()


def lumberstack():
    traceback.print_stack()
    print(repr(traceback.extract_stack()))
    print(repr(traceback.format_stack()))


another_function()

# -----------------------------
