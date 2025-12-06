def generate_repeated_numbers(max_val):
    candidates = set()
    max_digits = len(str(max_val))
    for half_len in range(1, (max_digits // 2) + 2):
        total_len = 2 * half_len
        if total_len > 12:  # safe upper bound (covers up to billions)
            break
        start = 10 ** (half_len - 1)
        end = 10 ** half_len - 1
        for base in range(start, end + 1):
            num = int(str(base) + str(base))
            if num > max_val:
                break
            candidates.add(num)
    return candidates


def main():
    with open('input.txt', 'r') as f:
        line = f.read().strip()

    ranges = []
    for part in line.split(','):
        if not part:
            continue
        a, b = part.split('-')
        ranges.append((int(a), int(b)))

    if not ranges:
        print(0)
        return

    max_end = max(end for _, end in ranges)
    invalid_ids = generate_repeated_numbers(max_end)

    total = 0
    for num in invalid_ids:
        for start, end in ranges:
            if start <= num <= end:
                total += num
                break  # count each ID once

    print(total)


if __name__ == '__main__':
    main()
