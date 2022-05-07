# p61 Manipulation with quote
quote = ' Lolipop for Barbie girl'
print(quote)
print(quote.upper())
print(quote.lower())
print(quote.title())
print(quote.replace('Lolipop', 'Banana'))
print(quote.swapcase())
print(quote.capitalize())
print(quote.strip())

# p64 Rentier(with fixed integer bug)
print('All payments')
carCost = int(input('Car Costs: '))
flatCost = int(input('Flat Costs: '))
foodCost = float(input('Food Costs: ')) #Float
total = carCost + flatCost + foodCost
print(total)
print(type(total)) #Shows a type. If last variable was float
#then after sums with other variables result will be float

# Important notice - in PyCharm ALt+4 opens current Run Terminal
# and closes it. It could be useful because
# you don`t touch the mouse.
# Although you could Run your program by Shift+10
# And new-file program by Ctrl+Shift+F10
# If you choose your file you could refactor/rename it
# by pressing Shift+F6

#p68
total2 = total * 12
print(total2)
# print(total *= 12) #Error will be. Master Yoda
total *= 12
print(total)
