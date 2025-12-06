def main():
    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f if line.strip()]

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

    count_accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            # Count adjacent '@' in 8 directions
            adjacent = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        adjacent += 1
            if adjacent < 4:
                count_accessible += 1

    print(count_accessible)


if __name__ == '__main__':
    main()
