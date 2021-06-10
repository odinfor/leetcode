#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 3:31 下午
# @Site    : 
# @File    : no459.py
# @desc    :
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        最长前缀: 子串必是字符串s的前缀，并且s的长度为子串的正数倍.并且最长子串长度<=len(s)//2
        """
        curr_s = str()
        if len(s) == 1:
            return True

        for i in range(len(s) // 2 + 1):
            curr_s += s[i]
            n = len(s) // len(curr_s)
            if len(s) % len(curr_s) != 0:
                continue
            if all(s[y * len(curr_s): (y + 1) * len(curr_s)] == curr_s for y in range(0, n)):
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.repeatedSubstringPattern("abab"))
    print(s.repeatedSubstringPattern("abc"))