#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 10:24 上午
# @Site    : 
# @File    : no56.py
# @desc    :
class Solution:
    def merge(self, intervals: list) -> list:
        """
        思路：先按左区间排序，然后遍历整理区间
        """
        intervals.sort(key=lambda x: x[0])
        merge_list = []

        for i in intervals:
            if not merge_list:
                merge_list.append(i)
                continue
            if merge_list[-1][0] <= i[0] <= merge_list[-1][1]:  # 更新最后一个合并值的右区间
                merge_list[-1][1] = max(i[1], merge_list[-1][1])
            elif i[0] >= merge_list[-1][0] and i[1] <= merge_list[-1][1]:   # 包含关系，不处理
                continue
            elif i[0] > merge_list[-1][1]:  # 插入区间
                merge_list.append(i)

        return merge_list


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))



