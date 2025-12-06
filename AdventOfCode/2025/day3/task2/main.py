def max_12_digit_joltage(bank: str) -> int:
    T = 12
    n = len(bank)
    if n <= T:
        # If exactly 12 or fewer, take all (but problem assumes >=12)
        return int(bank[:T])

    to_remove = n - T
    stack = []

    for digit in bank:
        # While we can remove, and stack has smaller digit at top
        while to_remove > 0 and stack and digit > stack[-1]:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    # If we still need to remove (e.g., non-increasing sequence)
    # Just take the first T digits
    result = ''.join(stack[:T])
    return int(result)


def main():
    with open('input.txt', 'r') as f:
        banks = [line.strip() for line in f if line.strip()]

    total = 0
    for bank in banks:
        total += max_12_digit_joltage(bank)

    print(total)


if __name__ == '__main__':
    main()
