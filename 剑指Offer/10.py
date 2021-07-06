#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 3:28 下午
# @Site    : 
# @File    : 10.py
# @desc    : 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
#            F(0) = 0,   F(1) = 1
#            F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        a, b = 0, 1

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b % 1000000007

    def fib2(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        curr = self.fib2(n - 1) + self.fib2(n - 2)

        return curr


if __name__ == "__main__":
    s = Solution()
    print(s.fib(45))
    print(s.fib2(6))