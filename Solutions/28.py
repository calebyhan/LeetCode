"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Python 3.12.2
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1