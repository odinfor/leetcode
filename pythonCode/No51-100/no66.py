#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/18 4:13 下午
# @Site    : 
# @File    : no66.py
# @desc    :
class Solution:
    def plusOne(self, digits: list) -> list:
        isNeedAddOne = False
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                sumNum = digits[i] + 1
                if sumNum < 10:
                    digits[i] = sumNum
                    isNeedAddOne = False
                    break
                else:
                    digits[i] = sumNum - 10
                    isNeedAddOne = True
                    continue
            if isNeedAddOne:
                sumNum = digits[i] + 1
                if sumNum < 10:
                    digits[i] = sumNum
                    isNeedAddOne = False
                    break
                else:
                    digits[i] = sumNum - 10
                    isNeedAddOne = True

        if isNeedAddOne:    # 需要进位
            digits = [1] + digits
            return digits
        else:
            return digits


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3, 4]))
    print(s.plusOne([0]))
    print(s.plusOne([1, 2, 3, 9]))
    print(s.plusOne([9, 9, 9]))

