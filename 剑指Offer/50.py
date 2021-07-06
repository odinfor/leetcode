#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 5:16 下午
# @Site    : 
# @File    : 50.py
# @desc    :
class Solution:
    def firstUniqChar(self, s: str) -> str:
        s_dict, min_index = dict(), 99999
        for i in s:
            s_dict[i] = s_dict.get(i, -2) + 1
        if not s_dict:
            return " "
        for k, v in s_dict.items():
            if v < 0:
                min_index = min(min_index, s.index(k))

        return s[min_index] if min_index != 99999 else " "


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("abaccdeff"))