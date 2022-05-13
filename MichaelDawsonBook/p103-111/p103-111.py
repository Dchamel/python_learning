# p105
word = 'Amphora'
for letter in word:
    print(letter)

# p108
for i in range(10):
    print(i, end='')
print('')
for i in range (0,50,5):
    print(i, end=' ')
print('')
for i in range(10, 0, -1):
    print(i, end=' ')
print('')

# p109
for _ in range(10):
    print('Ol', end='')
print('')

# p101
word = 'Collab`oration\t'
print(word,'-',len(word))
if 'b' in word:
    print('yes')
else:
    print('no')
