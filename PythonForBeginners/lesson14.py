# standart function 1
def rectangle_area(a,b):
    return a * b
print(rectangle_area(15, 12))

# lambda function 1
print((lambda a, b: a * b)(15, 12))

# standart function 2
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print(maximum(22, 24))

# lambda function 2
print((lambda a, b: a if a > b else b)(24, 22))