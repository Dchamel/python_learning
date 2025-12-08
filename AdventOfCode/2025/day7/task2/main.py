def main():
    with open('input.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    if not lines:
        print(0)
        return

    # Determine max width (including blank lines)
    max_width = max(len(line) for line in lines)
    rows = len(lines)
    cols = max_width

    # Create padded grid and find start position
    grid = []
    start_row = start_col = -1
    for r, line in enumerate(lines):
        padded_line = line.ljust(max_width, '.')
        if 'S' in padded_line:
            start_row = r
            start_col = padded_line.index('S')
        # Replace 'S' with '.' for simulation
        cleaned_line = padded_line.replace('S', '.')
        grid.append(cleaned_line)

    if start_row == -1 or start_col == -1:
        print(0)
        return

    # If starting on the last row, only one timeline
    if start_row == rows - 1:
        print(1)
        return

    # dp[r][c] = number of timelines starting from (r, c)
    dp = [[0] * cols for _ in range(rows)]

    # Base case: last row - all cells have exactly 1 timeline (beam exits immediately after)
    for c in range(cols):
        dp[rows - 1][c] = 1

    # Process from bottom to top (excluding the last row)
    for r in range(rows - 2, -1, -1):
        next_r = r + 1
        for c in range(cols):
            # Cell directly below current position
            cell_below = grid[next_r][c]

            if cell_below == '^':
                # Splitter: beam branches left and right
                left_col = c - 1
                right_col = c + 1

                # Left branch: exits immediately if out of bounds, else use dp value
                if left_col < 0 or left_col >= cols:
                    left_count = 1
                else:
                    left_count = dp[next_r][left_col]

                # Right branch
                if right_col < 0 or right_col >= cols:
                    right_count = 1
                else:
                    right_count = dp[next_r][right_col]

                dp[r][c] = left_count + right_count
            else:
                # Non-splitter: beam continues straight down
                dp[r][c] = dp[next_r][c]

    # Result is the number of timelines starting from the initial position
    print(dp[start_row][start_col])


if __name__ == '__main__':
    main()

# 357525737893560
