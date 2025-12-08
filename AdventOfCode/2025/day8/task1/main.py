import sys
from collections import defaultdict


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
    if n == 0:
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
    size = [1] * n  # Only valid for roots

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]

    def union(a, b):
        a_root = find(a)
        b_root = find(b)
        if a_root == b_root:
            return False
        # Union by size
        if size[a_root] < size[b_root]:
            a_root, b_root = b_root, a_root
        parent[b_root] = a_root
        size[a_root] += size[b_root]
        return True

    # Process the first 1000 edges (or all if fewer)
    num_edges_to_process = min(1000, len(edges))
    for idx in range(num_edges_to_process):
        _, i, j = edges[idx]
        if find(i) != find(j):
            union(i, j)

    # Compress paths for all nodes
    for i in range(n):
        find(i)

    # Count component sizes
    comp_sizes = defaultdict(int)
    for i in range(n):
        comp_sizes[parent[i]] += 1

    # Get sorted sizes (descending)
    sizes = sorted(comp_sizes.values(), reverse=True)

    # Multiply the three largest
    if len(sizes) < 3:
        result = 1
        for s in sizes:
            result *= s
    else:
        result = sizes[0] * sizes[1] * sizes[2]

    print(result)


if __name__ == '__main__':
    main()
