# btw in this file add some new thing not from the Micael`s book - time.
# Just to understand how fast some part of the code are working
# perf_counter() - returns float value of time in Seconds
# new func round
# and the method to "suppress" scientific notation for float values

from time import perf_counter

t0 = perf_counter() #save time before
print('Open the file')
file = open('readme.txt','r', encoding='utf-8')
#print 10 symbols from the beginning
print(file.read(14))
#the rest of the file
print(file.read())
file.close()
t1 = perf_counter() - t0 #save time after
# print(round(t1, 6))
print(f'{t1:.10f} sec')


file = open('readme.txt','r', encoding='utf-8')
lines = file.readlines()
chars = '~!@#$%^&*()_+{}:"<>?,./;\'][1234567890=\n№'

t0 = perf_counter()
lines2 = []
for element in lines:
    for char in chars:
        element = element.replace(char, '')
    lines2.append(element)
print(lines2)
t1 = perf_counter() - t0
# print(round(t1, 7))
print(f'{t1:.10f} sec')

t0 = perf_counter()
lines3 = []
for element in lines:
    element2 = element.maketrans(chars,chars,chars)
    element = element.translate(element2)
    lines3.append(element)
print(lines3)
t1 = perf_counter() - t0
# t1 = round(t1, 7)
print(f'{t1:.10f} sec')

# print(lines)
file.close()
