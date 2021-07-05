#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/2 3:08 下午
# @Site    : 
# @File    : no179.py
# @desc    :

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list) -> str:

        nums.sort(key=cmp_to_key(lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y))))
        ans = ''.join([str(num) for num in nums])
        return ans if not ans.startswith("0") else "0"


if __name__ == "__main__":
    s = Solution()
    # print(s.largestNumber([3, 30, 34, 5, 9]))
    # print(s.largestNumber([10,2,9,39,17]))
    print(s.largestNumber([1,2,4,8,16,32,64,128,256,512]))