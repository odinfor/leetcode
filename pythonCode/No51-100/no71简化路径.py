#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/11 4:12 下午
# @Site    : 
# @File    : no71简化路径.py
# @desc    : 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。

"""
示例1
输入：path = "/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。

示例2
输入：path = "/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根目录是你可以到达的最高级。

示例3
输入：path = "/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。

示例4
输入：path = "/a/./b/../../c/"
输出："/c"
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        s, stack = path.split("/"), []
        for i in range(1, len(s)):
            if not s[i]:
                continue
            elif s[i] == ".":
                continue
            elif s[i] == ".." and len(stack) >= 1:
                stack.pop(-1)
            elif s[i] == ".." and len(stack) == 0:
                continue
            else:
                stack.append(s[i])
        return "/" + "/".join(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/home/"))
    print(s.simplifyPath("/../"))
    print(s.simplifyPath("//home//foo/"))
    print(s.simplifyPath("//a/./b/../../c/"))

