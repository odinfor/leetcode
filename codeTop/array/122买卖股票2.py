#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 2:48 下午
# @Site    : 
# @File    : 122买卖股票2.py
# @desc    : 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
#            设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#            注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution:
    def maxProfit(self, prices: list) -> int:
        start, max_value = 0, 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            max_value = max_value + tmp if tmp > 0 else max_value

        return max_value


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([1,2,3,4,5]))