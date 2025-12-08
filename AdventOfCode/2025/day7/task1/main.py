def main():
    with open('input.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f if line.strip() != '' or line == '\n']

    if not lines:
        print(0)
        return

    # Determine maximum width and pad all lines with '.' to make a rectangle
    max_width = max(len(line) for line in lines)
    grid = [line.ljust(max_width, '.') for line in lines]
    rows = len(grid)

    # Find the starting position 'S'
    start_row, start_col = -1, -1
    for r in range(rows):
        if 'S' in grid[r]:
            start_row = r
            start_col = grid[r].index('S')
            break

    if start_row == -1:
        print(0)
        return

    # Set of column positions of active beams on the current row
    current_beams = {start_col}
    total_splits = 0

    # Process each row from the start row to the second-to-last row
    for r in range(start_row, rows - 1):
        next_beams = set()
        next_row = r + 1

        for c in current_beams:
            # Skip beams that have gone out of horizontal bounds
            if c < 0 or c >= max_width:
                continue

            # Check the cell directly below the beam
            cell_below = grid[next_row][c]

            if cell_below == '^':
                total_splits += 1
                # Emit new beams to the left and right of the splitter
                left_col = c - 1
                right_col = c + 1
                if left_col >= 0:
                    next_beams.add(left_col)
                if right_col < max_width:
                    next_beams.add(right_col)
            else:
                # Beam continues straight down
                next_beams.add(c)

        current_beams = next_beams
        if not current_beams:
            break  # No beams left to process

    print(total_splits)


if __name__ == '__main__':
    main()
