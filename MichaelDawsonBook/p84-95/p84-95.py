# p85
# print('Talk with child.')
# response = ''
# while response != 'That`s why !':
#     response = input('- Why ? \n- ')
# print('- Oh, Okay.')

# p87
# i = 0
# while i < 10:
#     i+=1
#     print(i)

# p87
# Battle Game
# health = 100
# trolls = 1
# damage = 7
# while health > 0:
#     print('Life:', health, 'Enemies:', trolls)
#     trolls += 1
#     health -= damage * trolls
# print('You`re dead')

# p89
# a = {0,1,2,-1,0.12,-0.12,+0,-0}
# for i in a:
#     print(bool(i))

# p90
# money = int(input('Value: '))
# if money:
#     print('Welcome')
# else:
#     print('You`re Not Welcome here')

# p92
# count = 0
# while True:
#     count+=1
#     if count > 10:
#         break
#     if count == 5:
#         continue
#     print(count)

# p95
username = ''
security = 0

while not bool(username):
    username = input('Username: ')
print(username)