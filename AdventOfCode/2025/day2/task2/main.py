def generate_all_repeated_numbers(max_val):
    if max_val < 10:
        return set()
    max_digits = len(str(max_val))
    candidates = set()

    # pattern length from 1 up to max_digits//2 (but allow up to max_digits for safety)
    for p_len in range(1, max_digits + 1):
        start = 10 ** (p_len - 1)
        end = 10 ** p_len - 1

        # If even the smallest repeat (k=2) has too many digits, break
        if 2 * p_len > 12:  # 12 digits is safe upper bound
            break

        for base in range(start, end + 1):
            base_str = str(base)
            repeated = base_str + base_str  # k = 2
            k = 2
            while len(repeated) <= 12:
                num = int(repeated)
                if num > max_val:
                    break
                candidates.add(num)
                # Add another repeat
                repeated += base_str
                k += 1
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
    invalid_ids = generate_all_repeated_numbers(max_end)

    total = 0
    for num in invalid_ids:
        for start, end in ranges:
            if start <= num <= end:
                total += num
                break  # avoid double-counting

    print(total)


if __name__ == '__main__':
    main()
