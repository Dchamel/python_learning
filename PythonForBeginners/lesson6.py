tuple = ('qwe', 12, 23.3,)
# tuple[1] = 50 #Cortege is non changeable
print(tuple)

tuple2 = ('qwer') #string type
tuple2 = ('qwer',) #tuple type
print(type(tuple2))

# print(tuple([12, 32, 56]))

print(list((12, 32, 56)))

# Dictionaries
dict = {'apple': 'red',
        'grape': 'green',
        'sky': 'dark'}
del(dict['sky'])
for k in dict.keys():
    print(k)

for k in dict.values():
    print(k)

for k in dict.items():
    print(k)
dict['grape'] = 'white'
print(dict['grape'])