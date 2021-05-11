#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 4:20 下午
# @Site    : 
# @File    : no415.py
# @desc    :
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 双指针，两个str从后往前
        if not num1:
            return num2
        if not num2:
            return num1
        indexNum1, indexNum2 = len(num1) - 1, len(num2) - 1
        resultList, needAddOne = [], False
        while True:
            value1 = int(num1[indexNum1]) if indexNum1 >= 0 else 0
            value2 = int(num2[indexNum2]) if indexNum2 >= 0 else 0
            if needAddOne:
                resultValue = value1 + value2 + 1
            else:
                resultValue = value1 + value2

            if resultValue > 10:
                resultList.append(str(resultValue - 10))
                needAddOne = True
            elif resultValue == 10:
                resultList.append("0")
                needAddOne = True
            else:
                resultList.append(str(resultValue))
                needAddOne = False

            indexNum1 -= 1
            indexNum2 -= 1

            if indexNum1 < 0 and indexNum2 < 0:
                break

        # 最后一位是否需要进位
        if needAddOne:
            resultList.append("1")
        # 翻转list得到结果
        return "".join(resultList[::-1])



