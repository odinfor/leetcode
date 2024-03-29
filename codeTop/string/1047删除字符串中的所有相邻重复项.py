#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 5:31 下午
# @Site    : 
# @File    : 1047删除字符串中的所有相邻重复项.py
# @desc    : 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
#            在 S 上反复执行重复项删除操作，直到无法继续删除，在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if stack[-1] == i:
                stack.pop(-1)
            else:
                stack.append(i)

        return "".join(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates("abbaca"))
