def max_joltage(bank: str) -> int:
    if len(bank) < 2:
        return 0
    max_first = int(bank[0])
    best = 0
    for j in range(1, len(bank)):
        digit_j = int(bank[j])
        candidate = 10 * max_first + digit_j
        if candidate > best:
            best = candidate
        if digit_j > max_first:
            max_first = digit_j
    return best


def main():
    with open('input.txt', 'r') as f:
        banks = [line.strip() for line in f if line.strip()]

    total = 0
    for bank in banks:
        total += max_joltage(bank)

    print(total)


if __name__ == '__main__':
    main()
