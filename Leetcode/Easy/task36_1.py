from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            nums2 = nums[:]
            del nums2[i]
            for num2 in nums2:
                if num + num2 == target:
                    return [num, num2]



nums = [2, 7, 11, 15]
target = 9

sol1 = Solution()
print(sol1.twoSum(nums, target))
