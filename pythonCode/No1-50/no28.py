#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/20 4:05 下午
# @Site    : 
# @File    : no28.py
# @desc    :

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        if not needle and haystack:
            return 0

        needleStartStrIndexList = []
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                needleStartStrIndexList.append(i)

        if not needleStartStrIndexList:
            return -1

        for i in needleStartStrIndexList:
            if haystack[i: i + len(needle)] == needle:
                return i


if __name__ == "__main__":
    s = Solution()
    s.strStr("hello", "ll")