#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 2:39 下午
# @Site    : 
# @File    : 121买卖股票.py
# @desc    : 给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。
#            你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#            返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

class Solution:
    def maxProfit(self, prices: list) -> int:
        left, max_price, max_index = 0, -99999, int()
        for i in range(1, len(prices)):
            if prices[left] >= prices[i]:
                left = i
                continue
            max_price = max(prices[i] - prices[left], max_price)

        return max_price if max_price != -99999 else 0


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))