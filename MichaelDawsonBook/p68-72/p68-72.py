# p71 Tasks
# Task2
food1 = input('Food Number one: ')
food2 = input('Food Number two: ')
print(food1+food2)

# Task3
finalCost = int(input('Final Cost: '))
tips1 = round(finalCost * 0.2)
print(tips1)

# Task4
# To buy a car
# Using a function here is exprompt
def finalCost(carCost):
    tax = round(carCost * 0.2)
    regFee = round(carCost * 0.13)
    agencyFee = round(carCost * 0.06)
    transportFee = 100
    return carCost + tax + regFee + agencyFee + transportFee

carCost = int(input('Input price for a car: '))
print('Final car Cost will be a',finalCost(carCost),'dollars')
