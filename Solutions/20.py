"""
https://leetcode.com/problems/valid-parentheses/

Python 3.12.2
"""

class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        if len(s) == 0:
            return True
        return False