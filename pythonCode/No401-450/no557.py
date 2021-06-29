#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 2:34 下午
# @Site    : 
# @File    : no557.py
# @desc    :
class Solution:
    def reverseWords(self, s: str) -> str:
        found_first, left_index = False, int()
        b = str()

        for i in range(len(s)):
            if s[i] == " " and not found_first:
                b += s[i]
            elif s[i] != " " and not found_first:
                if i != len(s) - 1:
                    left_index, found_first = i, True
                else:
                    b += s[i]
            elif s[i] == " " and found_first:
                b += s[left_index:i][::-1]
                b += s[i]
                found_first = False
            elif s[i] != " " and i == len(s) - 1:
                print(s[left_index:])
                b += s[left_index:][::-1]

        return b


if __name__ == "__main__":
    s = Solution()
    # print(s.reverseWords("Let's take LeetCode contest"))
    print(s.reverseWords("I love u"))
