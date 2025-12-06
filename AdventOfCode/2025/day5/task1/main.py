def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    # Split into two sections at the blank line
    try:
        blank_index = lines.index('')
    except ValueError:
        # In case there's no blank line (shouldn't happen per spec)
        blank_index = len(lines)

    ranges = []
    for line in lines[:blank_index]:
        if not line:
            continue
        a, b = map(int, line.split('-'))
        ranges.append((a, b))

    available = []
    for line in lines[blank_index + 1:]:
        if line:
            available.append(int(line))

    fresh_count = 0
    for ingredient_id in available:
        for start, end in ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break  # no need to check other ranges

    print(fresh_count)


if __name__ == '__main__':
    main()
