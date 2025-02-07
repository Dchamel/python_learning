import copy
from typing import List


# Given a circular array nums, find the maximum absolute difference between adjacent elements.
#
# Note: In a circular array, the first and last elements are adjacent.


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        """Calculates distance between adjacent elements"""

        nums.append(nums[0])
        new_nums = copy.deepcopy(nums)
        max_distance_list = []
        for i in range(len(nums) - 1):
            max_distance_list.append(abs(new_nums[i] - new_nums[i + 1]))

        return max(max_distance_list)


nums = [1, 2, 4]
nums = [-5, -10, -5]

print(Solution().maxAdjacentDistance(nums))
