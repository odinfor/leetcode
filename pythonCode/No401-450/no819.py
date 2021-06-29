#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 4:26 下午
# @Site    : 
# @File    : no819.py
# @desc    :
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        paragraph_dict, paragraph_list, s = dict(), list(), str()
        paragraph = paragraph.replace(" ", ";")

        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ").lower()
        paragraph_list = paragraph.strip().split()

        for p in paragraph_list:
            if p not in banned:
                paragraph_dict[p] = paragraph_dict.get(p, 0) + 1

        max_key, max_value = str(), int()
        for k, v in paragraph_dict.items():
            if v > max_value:
                max_value = v
                max_key = k

        return max_key


if __name__ == "__main__":
    s = Solution()
    print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
    print(s.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))


