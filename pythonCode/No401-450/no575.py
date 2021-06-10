#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 4:38 下午
# @Site    : 
# @File    : no575.py
# @desc    :
class Solution:
    def distributeCandies(self, candyType: list) -> int:
        candy_map, count = dict(), 0
        for i in candyType:
            if i in candy_map:
                candy_map[i] += 1
            else:
                candy_map[i] = 1

        for _ in sorted(candy_map.items(), key=lambda kv: (kv[1], kv[0])):
            count += 1
            if count == len(candyType) // 2:
                break

        return count

    def bySet(self, candyType: list) -> int:
        candy_set, every_count = set(candyType), len(candyType) // 2

        return every_count if len(candy_set) >= every_count else len(candy_set)


if __name__ == "__main__":
    s = Solution()
    print(s.distributeCandies([1,1,2,2,3,3]))
    print(s.bySet([1,1,2,3]))