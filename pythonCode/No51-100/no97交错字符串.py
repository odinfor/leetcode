#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 5:14 下午
# @Site    : 
# @File    : no97交错字符串.py
# @desc    :

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        elif not s1 and s2 == s3:
            return True
        elif not s2 and s1 == s3:
            return True

        res1, res2 = False, False
        diff_s1, diff_s2 = "", ""
        diff_index1, diff_index2 = 0, 0
        for i in s3:
            if diff_index1 >= len(s1):
                break
            if i != s1[diff_index1]:
                diff_s1 += i
            else:
                diff_index1 += 1
        if diff_s1 == s2:
            res1 = True

        for i in s3:
            if diff_index2 >= len(s2):
                break
            if i != s2[diff_index2]:
                diff_s2 += i
            else:
                diff_index2 += 1
        if diff_s2 == s1:
            res2 = True

        print(res1, res2)

        return True if res1 or res2 else False


if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))