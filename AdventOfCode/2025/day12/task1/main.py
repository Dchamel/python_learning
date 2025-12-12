# Shape areas
areas = [7, 7, 7, 5, 7, 6]

count = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if 'x' not in line:
            continue
        if ':' in line:
            dim, rest = line.split(':', 1)
        else:
            parts = line.split()
            dim, rest = parts[0], ' '.join(parts[1:])
        w, h = map(int, dim.split('x'))
        counts = list(map(int, rest.split()))
        total_area = sum(counts[i] * areas[i] for i in range(len(counts)))
        if total_area <= w * h:
            count += 1
print(count)
