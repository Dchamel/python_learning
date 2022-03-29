numbers = {1, 5, 2, 10, 11, 9, 23, 12}
print(numbers)
numbers = {}
print(type(numbers))  #dictionary
numbers = set()
print(type(numbers))  #set

numbers = {1, 5, 2, 10, 11, 9, 23, 12}
for i in numbers:
    print(i)
print(5 in numbers) #True or False
numbers.add(45)
print(numbers)
numbers.discard(111) # without error
# numbers.remove(111) with error
numbers.pop() # delete FIRST element
numbers.clear()
print(numbers)

numbers1 = {1, 5, 2, 10, 11, 9, 23, 12}
numbers2 = {2, 33, 12, 5, 7, 45, 21, 11, 99}
numbers3 = numbers1.union(numbers2)
print(numbers3)
numbers3 = numbers2 - numbers1
print(numbers3)
numbers3 = numbers2
numbers3.add(111)
print(numbers2)
print(numbers3, '\n')
numbers3 = numbers2.copy()
numbers2.add(222)
print(numbers2)
print(numbers3)

numbers1 = frozenset({1, 5, 2, 10, 11, 9, 23, 12})
print(numbers1)
# numbers1.add(11) Will be an error

