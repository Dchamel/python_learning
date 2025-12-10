def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    reds = []
    for line in lines:
        parts = line.split(',')
        x = int(parts[0])
        y = int(parts[1])
        reds.append((x, y))

    n = len(reds)
    if n < 2:
        print(0)
        return

    # Build vertical edges: (x, y_start, y_end) with y_start < y_end
    vertical_edges = []
    for i in range(n):
        x1, y1 = reds[i]
        x2, y2 = reds[(i + 1) % n]
        if x1 == x2 and y1 != y2:
            y_start = min(y1, y2)
            y_end = max(y1, y2)
            vertical_edges.append((x1, y_start, y_end))

    # Find y range
    all_y = [y for _, y in reds]
    min_y = min(all_y)
    max_y = max(all_y)

    # For each y, collect x coordinates of vertical edges that cross it (using [y_start, y_end))
    from collections import defaultdict
    crossings = defaultdict(list)
    for x, y_start, y_end in vertical_edges:
        # Use half-open interval [y_start, y_end) to avoid double-counting
        for y in range(y_start, y_end):
            crossings[y].append(x)

    # Build intervals for each y
    row_intervals = {}
    for y in range(min_y, max_y + 1):
        xs = crossings.get(y, [])
        if not xs:
            continue
        xs = sorted(set(xs))
        if len(xs) % 2 != 0:
            # Should not happen in closed loop, but skip to be safe
            continue
        intervals = []
        for i in range(0, len(xs), 2):
            intervals.append((xs[i], xs[i + 1]))
        row_intervals[y] = intervals

    # Now check all pairs of red points
    max_area = 0
    for i in range(n):
        x1, y1 = reds[i]
        for j in range(i + 1, n):
            x2, y2 = reds[j]
            rx1, rx2 = min(x1, x2), max(x1, x2)
            ry1, ry2 = min(y1, y2), max(y1, y2)

            valid = True
            for y in range(ry1, ry2 + 1):
                if y not in row_intervals:
                    # This row has no interior — likely outside the loop
                    valid = False
                    break
                covered = False
                for (ix1, ix2) in row_intervals[y]:
                    if ix1 <= rx1 and rx2 <= ix2:
                        covered = True
                        break
                if not covered:
                    valid = False
                    break

            if valid:
                area = (rx2 - rx1 + 1) * (ry2 - ry1 + 1)
                if area > max_area:
                    max_area = area

    print(max_area)


if __name__ == '__main__':
    main()
