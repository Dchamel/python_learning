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

# bisect
# insert to ordered list
import bisect

# example1
ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bisect.bisect_left(ordered_list, 2))
print(bisect.bisect_right(ordered_list, 2))
print(ordered_list)
print(bisect.insort_left(ordered_list, 2))
print(ordered_list)


# example2
def grade(score, breakpoints=[30, 40, 50, 60], grades='ABC'):
    i = bisect(breakpoints, score)
    return grades[i]


print([grade(score) for score in [32, 43, 11, 40, 20, 200]])

# -----------------------------
