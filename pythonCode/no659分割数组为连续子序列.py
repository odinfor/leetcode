#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 4:01 下午
# @Site    : 
# @File    : no659分割数组为连续子序列.py
# @desc    : 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个长度至少为 3 的子序列，其中每个子序列都由连续整数组成
#            如果可以完成上述分割，则返回 true ；否则，返回 false
import collections

class Solution:
    def isPossible(self, nums: list) -> bool:
        countMap = collections.Counter(nums)
        endMap = collections.Counter()

        for x in nums:
            if (count := countMap[x]) > 0:
                if (prevEndCount := endMap.get(x - 1, 0)) > 0:
                    countMap[x] -= 1
                    endMap[x - 1] = prevEndCount - 1
                    endMap[x] += 1
                else:
                    if (count1 := countMap.get(x + 1, 0)) > 0 and (count2 := countMap.get(x + 2, 0)) > 0:
                        countMap[x] -= 1
                        countMap[x + 1] -= 1
                        countMap[x + 2] -= 1
                        endMap[x + 2] += 1
                    else:
                        return False

        return True


