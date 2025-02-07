from typing import List


# You are given an integer array nums of size n. For each index i where 0 <= i < n, define a
# subarray nums[start ... i] where start = max(0, i - nums[i]).
#
# Return the total sum of all elements from the subarray defined for each index in the array.


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total_sum = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            sub_nums = sum(nums[start:i + 1])
            total_sum += sub_nums

        return total_sum


nums = [2, 3, 1]

print(Solution().subarraySum(nums))
