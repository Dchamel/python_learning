def readData():
    with open('inputs/task1.txt', 'r') as rawData:
        data = rawData.read()
    return data

def task1():
    lvl = 0
    for each in readData():
        if each == '(':
            lvl += 1
        else:
            lvl -= 1
    return lvl

print(task1())