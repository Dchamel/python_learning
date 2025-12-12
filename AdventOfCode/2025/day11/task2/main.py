import sys
from collections import defaultdict
from functools import lru_cache


def solve() -> None:
    graph = defaultdict(list)
    with open('input.txt', 'r') as f:
        for line in f:
            if not line.strip():
                continue
            node, _, neighbors = line.partition(':')
            node = node.strip()
            graph[node] = neighbors.strip().split()

    sys.setrecursionlimit(10000)

    @lru_cache(maxsize=None)
    def count_paths(node: str, has_fft: bool, has_dac: bool) -> int:
        if node == 'out':
            return 1 if (has_fft and has_dac) else 0
        total = 0
        for nxt in graph[node]:
            new_fft = has_fft or (nxt == 'fft')
            new_dac = has_dac or (nxt == 'dac')
            total += count_paths(nxt, new_fft, new_dac)
        return total

    result = count_paths('svr', False, False)
    print(result)


if __name__ == "__main__":
    solve()
