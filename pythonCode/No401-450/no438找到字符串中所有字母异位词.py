#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 5:49 下午
# @Site    : 
# @File    : no438找到字符串中所有字母异位词.py
# @desc    :
class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        mapTarget, lens, lenp, startList = {}, len(s), len(p), []
        if lenp > lens:
            return startList
        for i in p:
            if mapTarget.get(i):
                mapTarget[i] += 1
            else:
                mapTarget[i] = 1
        left = 0
        newMap = dict()
        while left <= lens - lenp:
            if left == 0:
                for i in range(lenp):
                    if newMap.get(s[i]):
                        newMap[s[i]] += 1
                    else:
                        newMap[s[i]] = 1
            else:
                newMap[s[left - 1]] -= 1
                if newMap[s[left - 1]] == 0:
                    newMap.pop(s[left - 1])
                if newMap.get(s[left + lenp - 1]):
                    newMap[s[left + lenp - 1]] += 1
                else:
                    newMap[s[left + lenp - 1]] = 1
            if newMap == mapTarget:
                startList.append(left)
            left += 1
        return startList


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagrams("abacbabc", "abc"))
