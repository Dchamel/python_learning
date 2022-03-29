spisok = []
numbers = [1, 3, 5, 9, 11, 23]
print(numbers)

numbers = [2, 3, 55, 'Vovan']
print(numbers)

numbers = [5, 22, 5123125, 'Kirill', [453, 11], ['Lola', 'Nika']]
print(numbers)

print(numbers[-1])

numbers.append('Кулак')
numbers.insert(1, 'Kir')
numbers.pop() #What happen if i`ll add a number in pop() ?

for value in numbers:
    print(value)

print(numbers.index('Kirill'))
print(len(numbers))

numbers = [1, 22,434, 12, 54, 634636, 32453, 14, 32]
numbers.sort()
print(numbers)