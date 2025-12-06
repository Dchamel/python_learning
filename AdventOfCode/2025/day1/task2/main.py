def count_zeros_in_rotation(pos, direction, d):
    if direction == 'R':
        target = (100 - pos) % 100
    else:  # 'L'
        target = pos % 100

    if target == 0:
        first = 100
    else:
        first = target

    if first > d:
        return 0
    else:
        return 1 + (d - first) // 100


# Main
pos = 50
total = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        d = int(line[1:])
        total += count_zeros_in_rotation(pos, direction, d)
        # Update position
        if direction == 'R':
            pos = (pos + d) % 100
        else:
            pos = (pos - d) % 100

print(total)
