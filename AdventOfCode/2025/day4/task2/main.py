def main():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    if not grid:
        print(0)
        return

    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    total_removed = 0

    while True:
        to_remove = []
        # Scan entire grid to find removable rolls (based on current state)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '@':
                    continue
                # Count adjacent '@'
                adjacent = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            adjacent += 1
                if adjacent < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break

        # Remove all marked rolls
        for r, c in to_remove:
            grid[r][c] = '.'
        total_removed += len(to_remove)

    print(total_removed)


if __name__ == '__main__':
    main()
