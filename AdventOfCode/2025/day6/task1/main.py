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

    # Identify blank columns (all spaces)
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

    total_grand = 0

    for start, end in problems:
        numbers = []
        operator = None
        for r in range(rows):
            segment = grid[r][start:end].rstrip()
            if not segment:
                continue
            if r == rows - 1:
                # Last row: operator
                if segment in ('+', '*'):
                    operator = segment
                # Ignore anything else (shouldn't happen)
            else:
                # Parse number
                try:
                    num = int(segment)
                    numbers.append(num)
                except ValueError:
                    # Skip malformed (shouldn't happen)
                    pass

        if not numbers or operator is None:
            continue

        # Apply operation
        if operator == '+':
            result = sum(numbers)
        elif operator == '*':
            result = 1
            for n in numbers:
                result *= n
        else:
            continue

        total_grand += result

    print(total_grand)


if __name__ == '__main__':
    main()
