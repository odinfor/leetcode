#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 3:24 下午
# @Site    : 
# @File    : no1619删除某些元素后的数组均值.py
# @desc    :

class Solution:
    def trimMean(self, arr: list) -> float:
        arr.sort()
        s, l = sum(arr), len(arr)
        deleteNum = int(l * 0.05)
        return sum(arr[deleteNum: l - deleteNum])/(l - 2 * deleteNum)


if __name__ == "__main__":
    s = Solution()
    print(s.trimMean([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))