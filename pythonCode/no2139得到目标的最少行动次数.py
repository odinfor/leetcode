#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 6:39 下午
# @Site    : 
# @File    : no2139得到目标的最少行动次数.py
# @desc    :

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count, mid = 0, target
        if maxDoubles == 0:
            return target - 1

        while maxDoubles:
            if mid == 1:
                return count
            if mid % 2:
                count += 1
                mid = mid - 1
            else:
                count += 1
                mid = mid // 2
                maxDoubles -= 1

        return count + mid - 1


if __name__ == "__main__":
    s = Solution()
    print(s.minMoves(19, 2))
    print(s.minMoves(10, 4))