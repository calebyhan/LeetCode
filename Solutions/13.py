"""
https://leetcode.com/problems/roman-to-integer/

Python 3.12.2
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            if s[i] == "I":
                if len(s) - 1 != i:
                    if s[i + 1] == "V":
                        ret += 4
                    elif s[i + 1] == "X":
                        ret += 9
                    else:
                        ret += 1
                else:
                    ret += 1
            if s[i] == "V":
                if i != 0:
                    if s[i - 1] != "I":
                        ret += 5
                else:
                    ret += 5
            if s[i] == "X":
                if len(s) - 1 != i:
                    if s[i + 1] == "L":
                        ret += 40
                    elif s[i + 1] == "C":
                        ret += 90
                    else:
                        if i != 0:
                            if s[i - 1] != "I":
                                ret += 10
                        else:
                            ret += 10
                else:
                    if i != 0:
                        if s[i - 1] != "I":
                            ret += 10
                    else:
                        ret += 10
            if s[i] == "L":
                if i != 0:
                    if s[i - 1] != "X":
                        ret += 50
                else:
                    ret += 50
            if s[i] == "C":
                if len(s) - 1 != i:
                    if s[i + 1] == "D":
                        ret += 400
                    elif s[i + 1] == "M":
                        ret += 900
                    else:
                        if i != 0:
                            if s[i - 1] != "X":
                                ret += 100
                        else:
                            ret += 100
                else:
                    if i != 0:
                        if s[i - 1] != "X":
                            ret += 100
                    else:
                        ret += 100
            if s[i] == "D":
                if i != 0:
                    if s[i - 1] != "C":
                        ret += 500
                else:
                        ret += 500
            if s[i] == "M":
                if i != 0:
                    if s[i - 1] != "C":
                        ret += 1000
                else:
                        ret += 1000

        return ret