#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 3:49 下午
# @Site    : 
# @File    : no409.py
# @desc    :
class Solution:
    def longestPalindrome(self, s: str) -> int:
        str_map, has_only_str, str_long = dict(), False, int()
        for i in s:
            if i in str_map:
                str_map[i] += 1
            else:
                str_map[i] = 1

        for k, v in str_map.items():
            if v % 2 == 1:
                str_long = str_long + (v // 2) * 2
                has_only_str = True
            else:
                str_long += v

        if has_only_str:
            str_long += 1

        return str_long


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))