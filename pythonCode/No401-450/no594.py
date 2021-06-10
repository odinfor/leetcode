#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 5:57 下午
# @Site    : 
# @File    : no594.py
# @desc    :
class Solution:
    def findLHS(self, nums: list) -> int:
        num_map, res = dict(), 0
        for i in nums:
            num_map[i] = num_map.get(i, 0) + 1

        for i in num_map:
            if not num_map.get(i) or not num_map.get(i + 1):
                continue
            res = max(res, num_map.get(i) + num_map.get(i + 1, 0))

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findLHS([1,3,2,2,5,2,3,7]))
    print(s.findLHS([1,1,1,1]))