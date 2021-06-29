#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 5:01 下午
# @Site    : 
# @File    : no859.py
# @desc    :
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            common_set = set()
            for i in s:
                common_set.add(i)
            return True if len(common_set) < len(s) else False

        diff_index, start_index = list(), int()
        while start_index <= len(s) - 1:
            if s[start_index] != goal[start_index]:
                diff_index.append(start_index)
            start_index += 1

        if len(diff_index) > 2 or len(diff_index) < 2:
            return False

        return True if s[diff_index[0]] == goal[diff_index[1]] and s[diff_index[1]] == goal[diff_index[0]] else False


if __name__ == "__main__":
    s = Solution()
    print(s.buddyStrings("aa", "aa"))
    print(s.buddyStrings("ab", "ba"))
    print(s.buddyStrings("ab", "ab"))
    print(s.buddyStrings("aaaaaaabc", "aaaaaaacb"))
    print(s.buddyStrings("abccccc", "abccccc"))


