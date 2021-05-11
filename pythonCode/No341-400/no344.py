#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 3:35 下午
# @Site    : 
# @File    : no344.py
# @desc    :
class Solution:

    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or len(s) == 1:
            print(s)
            return
        # O1空间复杂度，双向指针
        left, right = 0, len(s) - 1
        while True:
            if left >= right:
                break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)

    def reverseString1(self, s):
        # 使用栈
        # for 入栈
        # for 出栈
        pass


if __name__ == "__main__":
    s = Solution()
    s.reverseString(["h","e","l","l","o"])
    s.reverseString(["H","a","n","n","a","h"])