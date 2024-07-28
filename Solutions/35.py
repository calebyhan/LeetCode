"""
https://leetcode.com/problems/search-insert-position/

Python 3.12.2
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)