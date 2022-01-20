#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/20 4:05 下午
# @Site    : 
# @File    : no28.py
# @desc    :

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # O(n)时间复杂度，
        if haystack == needle:
            return 0

        if not needle and haystack:
            return 0

        # 获得needle第一个元素在haystack中出现的索引位置
        needleStartStrIndexList = []
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                needleStartStrIndexList.append(i)

        if not needleStartStrIndexList:
            return -1

        # 判断haystack索引位置开始到needle长度的str是否和needle相同
        for i in needleStartStrIndexList:
            if haystack[i: i + len(needle)] == needle:
                return i

        return -1


if __name__ == "__main__":
    s = Solution()
    s.strStr("hello", "ll")