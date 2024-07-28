"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Python 3.12.2
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums1 = sorted(list(set(nums)))
        for i in range(len(nums1)):
            nums[i] = nums1[i]
        return len(nums1)