def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    try:
        blank_index = lines.index('')
    except ValueError:
        blank_index = len(lines)

    ranges = []
    for line in lines[:blank_index]:
        if line:
            a, b = map(int, line.split('-'))
            ranges.append((a, b))

    if not ranges:
        print(0)
        return

    # Sort by start
    ranges.sort()

    # Merge overlapping intervals (inclusive)
    merged = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end:  # overlapping or contained
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    total = 0
    for start, end in merged:
        total += (end - start + 1)

    print(total)


if __name__ == '__main__':
    main()
