"""
https://leetcode.com/problems/remove-element/

Python 3.12.2
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums1 = []
        for i in nums:
            if i != val:
                nums1.append(i)
        for i in range(len(nums1)):
            nums[i] = nums1[i]
        return len(nums1)