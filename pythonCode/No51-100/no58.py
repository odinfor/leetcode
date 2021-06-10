#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 6:15 下午
# @Site    : 
# @File    : no58.py
# @desc    :
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = str()
        for i in s[::-1]:
            if i == " " and not res:
                continue
            if i == " " and res:
                break
            res = i + res

        return len(res)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("hello  world"))
    print(s.lengthOfLastWord("  "))