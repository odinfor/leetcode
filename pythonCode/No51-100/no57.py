#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 10:45 上午
# @Site    : 
# @File    : no57.py
# @desc    :
class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)

        if not placed:
            ans.append([left, right])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1, 3], [6, 9]], [2, 5]))
    print(s.insert([[1,2], [3,5], [6,7], [8,10], [12,16]], [4,8]))
    print(s.insert([[1, 5]], [2, 7]))



