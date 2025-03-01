"""
https://leetcode.com/problems/longest-common-prefix/

Python 3.12.2
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ret = ""
        for i in range(len(min(strs, key = len))):
            r = True
            for j in strs:
                if strs[0][i] != j[i]:
                    r = False
                    break
            if r:
                ret += strs[0][i]
            if not r:
                break
        return ret