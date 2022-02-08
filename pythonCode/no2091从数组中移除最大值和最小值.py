#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 6:05 下午
# @Site    : 
# @File    : no2091从数组中移除最大值和最小值.py
# @desc    : 给你一个下标从 0 开始的数组 nums ，数组由若干 互不相同 的整数组成。

class Solution:
    def minimumDeletions(self, nums: list) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2
        numsNew = sorted(nums)
        maxNumIndex, minNumIndex = nums.index(numsNew[-1]), nums.index(numsNew[0])

        time1 = min(max(minNumIndex, maxNumIndex) + 1, len(nums) - min(minNumIndex, maxNumIndex))
        time2 = min(minNumIndex + 1 + len(nums) - maxNumIndex, maxNumIndex + 1 + len(nums) - minNumIndex)

        return min(time1, time2)


if __name__ == "__main__":
    s = Solution()
    print(s.minimumDeletions([2,10,7,5,4,1,8,6]))
    print(s.minimumDeletions([0,-4,19,1,8,-2,-3,5]))
    print(s.minimumDeletions([-14,61,29,-18,59,13,-67,-16,55,-57,7,74]))