print('Open the file')
file = open('readme.txt','r', encoding='utf-8')
#print 10 symbols from the beginning
print(file.read(14))
#the rest of the file
print(file.read())
file.close()

file = open('readme.txt','r', encoding='utf-8')
lines = file.readlines()
lines2 = []
chars = '~!@#$%^&*()_+{}:"<>?,./;\'][1234567890'
for element in lines:

    element = element.replace(chars,'')
    lines2.append(element)
print(lines2)
file.close()
