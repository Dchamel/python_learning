# without generator. Traditional way
a = []
for i in range(1,21):
    if i % 5 == 0:
        a.append(i)
print(a)

# The same s.. thing, but created as generator
a1 = [i for i in range(1,21) if i%5==0]
print(a1)

# The same s.. thing, but with some calculations
a1 = [i**3 for i in range(1,21) if i%5==0]
print(sum(a1))

# nested list (branching) Traditional Way
a2 = []
for i in range(1, 21):
    for j in range(1, 51):
        a2.append((i, j))
print(a2)

# nested list (branching) Generator Way
a2 = [(i,j) for i in range(1,21) for j in range(1,51)]
print(a2)

# list with "else"
a3 = []
for i in range(-10,11):
    if (i > 0):
        a3.append(i**2)
    else:
        a3.append(i**3)
print(a3)

# generator with else and another 'if' in the end
a3 = [i**2 if i>0 else i**3 for i in range (-10,11) if i%2==0]
print(a3)

# the same but each part of it from new line
a3 = [i**2
      if i>0
      else i**3
      for i in range (-10,11)
      if i%2==0]
print(a3)

s = [1,2,3,4,2,1]
set_set = {i for i in s}
print (set_set)

dictionary = {i: i**10 for i in s}
print(dictionary)

