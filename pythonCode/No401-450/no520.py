#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 6:30 下午
# @Site    : 
# @File    : no520.py
# @desc    :
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        FirstBig, type_num = False, dict()
        for i in range(len(word)):
            if i == 0 and "A" <= word[i] <= "Z":
                FirstBig = True
                type_num["big"] = type_num.get("big", 0) + 1
            elif i != 0 and "A" <= word[i] <= "Z":
                type_num["big"] = type_num.get("big", 0) + 1
            elif "a" <= word[i] <= "z":
                type_num["small"] = type_num.get("small", 0) + 1
        if FirstBig and type_num["big"] == 1:
            return True
        elif FirstBig and type_num["big"] == len(word):
            return True
        elif not FirstBig and type_num["small"] == len(word):
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    # print(s.detectCapitalUse("USA"))
    print(s.detectCapitalUse("FlaG"))
    # print(s.detectCapitalUse("g"))
    # print(s.detectCapitalUse("Google"))