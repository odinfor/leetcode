#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/25 4:05 下午
# @Site    : 
# @File    : 002二进制加法.py
# @desc    : 给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。输入为 非空 字符串且只包含数字 1 和 0

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index_a, index_b, add_value, res = len(a) - 1, len(b) - 1, 0, ""
        while True:
            if index_a < 0 and index_b < 0:
                break
            curr_a = int(a[index_a]) if index_a >= 0 else 0
            curr_b = int(b[index_b]) if index_b >= 0 else 0
            curr_value = curr_a + curr_b + add_value
            if curr_value >= 2:
                add_value = 1
                res = str(curr_value - 2) + res
            else:
                add_value = 0
                res = str(curr_value) + res

            index_a -= 1
            index_b -= 1

        if add_value != 0:
            res = str(add_value) + res
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("10", "11"))
