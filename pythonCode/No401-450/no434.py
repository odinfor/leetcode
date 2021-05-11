#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 4:04 下午
# @Site    : 
# @File    : no434.py
# @desc    :
class Solution:
    def countSegments(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        is_dc_start, num = False, 0
        for i in s:
            if i != " " and not is_dc_start:   # 单词开头
                is_dc_start = True
            if is_dc_start and i == " ":       # 单词结尾
                num += 1
                is_dc_start = False
        if is_dc_start:     # 以单词结尾，num加1
            num += 1
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.countSegments("Hello, my name  is John"))
