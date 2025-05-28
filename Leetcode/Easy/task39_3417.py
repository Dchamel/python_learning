# You are given an m x n 2D array grid of positive integers.
#
# Your task is to traverse grid in a zigzag pattern while skipping every alternate cell.
#
# Zigzag pattern traversal is defined as following the below actions:
#
# Start at the top-left cell (0, 0).
# Move right within a row until the end of the row is reached.
# Drop down to the next row, then traverse left until the beginning of the row is reached.
# Continue alternating between right and left traversal until every row has been traversed.
# Note that you must skip every alternate cell during the traversal.
#
# Return an array of integers result containing, in order, the value of the cells visited during the zigzag traversal with skips.

from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        """
        Zigzag Traversal
        We can do it by two alg: one_by_one+1 and alg even_odd
        """
        # even_odd alg
        for i, line in enumerate(grid):
            if i % 2 != 0:
                print(i)


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(Solution().zigzagTraversal(grid))
