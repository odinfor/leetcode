#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 5:59 下午
# @Site    : 
# @File    : 14.py
# @desc    :
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return 1
        a, b, c = 1, 1, 1
        number, y_number = (n - 3) // 3, (n - 3) % 3

        if y_number == 0:
            return (a + number) * (b + number) * (c + number)
        elif y_number == 1:
            return (a + number) * (b + number) * (c + number + y_number)
        else:
            return (a + number) * (b + number + y_number) * (c + number + y_number)


if __name__ == "__main__":
    s = Solution()
    print(s.cuttingRope(10))

