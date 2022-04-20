#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 4:15 下午
# @Site    : 
# @File    : no1344时钟指针的夹角.py
# @desc    :

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        base_min_d, base_hour_d = 360 / 60, 360 / 12
        # 以0点位置作为起始
        hour_d = hour * base_hour_d + (minutes / 60) * base_hour_d
        min_d = minutes * base_min_d
        dif_d = abs(min_d - hour_d)
        return min(dif_d, 360 - dif_d)