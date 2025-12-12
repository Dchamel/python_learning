import sys
from collections import defaultdict


def count_paths(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    if start == end:
        return 1

    total = 0
    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            total += count_paths(graph, neighbor, end, visited)
            visited.remove(neighbor)
    return total


def solve():
    graph = defaultdict(list)

    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(':')
            device = parts[0].strip()
            outputs = parts[1].strip().split()
            graph[device] = outputs

    result = count_paths(graph, 'you', 'out')
    print(result)


if __name__ == "__main__":
    solve()
