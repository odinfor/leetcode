#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 4:35 下午
# @Site    : 
# @File    : no220.py
# @desc    :
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        left, len_num = 0, len(nums)
        if len_num < 2 or t < 0:
            return False

        while left + k < len_num:
            new_nums, nums_map = nums[left: left + k + 1], dict()
            for i in new_nums:
                if nums_map.get(i):
                    return True
                else:
                    nums_map[i] = 1
            for y in nums_map:
                if y + t in nums_map or y - t in nums_map:
                    return True
            left += 1

        return False


if __name__ == "__main__":
    s = Solution()
    # print(s.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
    # print(s.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
    # print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
    # print(s.containsNearbyAlmostDuplicate([2147483647,-1,2147483647], 1, 2147483647))
    print(s.containsNearbyAlmostDuplicate([8,7,15,1,6,1,9,15], 1, 3))