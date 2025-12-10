def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    points = []
    for line in lines:
        parts = line.split(',')
        if len(parts) < 2:
            continue
        x = int(parts[0])
        y = int(parts[1])
        points.append((x, y))

    n = len(points)
    if n < 2:
        print(0)
        return

    max_area = 0
    # Check all pairs of distinct points
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            area = (dx + 1) * (dy + 1)
            if area > max_area:
                max_area = area

    print(max_area)


if __name__ == '__main__':
    main()
