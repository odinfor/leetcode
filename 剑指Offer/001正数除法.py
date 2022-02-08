#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/24 4:54 下午
# @Site    : 
# @File    : 001正数除法.py
# @desc    : 给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。

class Solution:
    def divide(self, a: int, b: int) -> int:
        # 投机方法: 使用整除，注意除不尽时计算机为向下取整导致负数结果会有偏差,计算时转为正数进行计算
        res = abs(a) // abs(b)
        if (a > 0 and b < 0) or (a < 0 and b > 0):
            return 0 - res
        else:
            return res if res < 2 ** 31 else res - 1

    def divide2(self, a: int, b: int) -> int:
        # 循环减法
        dif_time, abs_a, abs_b = 0, abs(a), abs(b)
        res = abs_a
        if a == 0:
            return 0
        elif b == 1 or b == -1:
            dif_time = abs_a
        else:
            while res >= abs_b:
                dif_time += 1
                res -= abs_b

        if (a > 0 and b < 0) or (a < 0 and b > 0):
            return 0 - dif_time
        else:
            return dif_time if dif_time < 2 ** 31 else dif_time - 1
