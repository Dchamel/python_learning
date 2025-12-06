position = 50
count = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        if position == 0:
            count += 1

print(count)
