def main():
    with open('input.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f if line.rstrip('\n')]

    if not lines:
        print(0)
        return

    # Pad all lines to same length
    max_len = max(len(line) for line in lines)
    grid = [line.ljust(max_len) for line in lines]
    rows = len(grid)
    cols = max_len

    # Identify blank columns
    is_blank = [True] * cols
    for c in range(cols):
        for r in range(rows):
            if grid[r][c] != ' ':
                is_blank[c] = False
                break

    # Group contiguous non-blank columns
    problems = []
    c = 0
    while c < cols:
        if not is_blank[c]:
            start = c
            while c < cols and not is_blank[c]:
                c += 1
            end = c
            problems.append((start, end))
        else:
            c += 1

    grand_total = 0

    for start, end in problems:
        # Find operator in last row within this block
        operator = None
        for c in range(start, end):
            ch = grid[rows - 1][c]
            if ch in '+*':
                operator = ch
                break
        if operator is None:
            continue

        numbers = []
        # Each column in the block is one number (top to bottom, excluding last row)
        for c in range(start, end):
            digits = []
            for r in range(rows - 1):  # exclude operator row
                ch = grid[r][c]
                if ch != ' ':
                    digits.append(ch)
            if digits:
                num = int(''.join(digits))
                numbers.append(num)

        if not numbers:
            continue

        # Read columns right-to-left: reverse the list
        numbers = numbers[::-1]

        # Apply operation
        if operator == '+':
            result = sum(numbers)
        elif operator == '*':
            result = 1
            for n in numbers:
                result *= n
        else:
            continue

        grand_total += result

    print(grand_total)


if __name__ == '__main__':
    main()
