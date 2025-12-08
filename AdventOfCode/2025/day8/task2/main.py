import sys


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    points = []
    for line in lines:
        parts = line.split(',')
        if len(parts) < 3:
            continue
        x, y, z = map(int, parts[:3])
        points.append((x, y, z))

    n = len(points)
    if n <= 1:
        print(0)
        return

    # Precompute all pairwise squared distances
    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist_sq = dx * dx + dy * dy + dz * dz
            edges.append((dist_sq, i, j))

    # Sort edges by distance
    edges.sort(key=lambda x: x[0])

    # Union-Find (DSU) setup
    parent = list(range(n))
    rank = [0] * n

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        a_root = find(a)
        b_root = find(b)
        if a_root == b_root:
            return False
        if rank[a_root] < rank[b_root]:
            parent[a_root] = b_root
        elif rank[a_root] > rank[b_root]:
            parent[b_root] = a_root
        else:
            parent[b_root] = a_root
            rank[a_root] += 1
        return True

    # Track components and the final edge
    components = n
    final_edge = None

    for dist_sq, i, j in edges:
        if components == 1:
            break
        if find(i) != find(j):
            union(i, j)
            components -= 1
            if components == 1:
                final_edge = (i, j)
                break

    if final_edge is None:
        print(0)
        return

    i, j = final_edge
    x_i = points[i][0]
    x_j = points[j][0]
    result = x_i * x_j
    print(result)


if __name__ == '__main__':
    main()
