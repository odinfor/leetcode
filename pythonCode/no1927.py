#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/22 3:33 下午
# @Site    : 
# @File    : no1927.py
# @desc    :

class Solution:
    def sumGame(self, num: str) -> bool:
        left, right, maxLeft, maxRight, leftNum, rightNum = 0, len(num) - 1, 0, 0, 0, 0
        while left < right:
            if num[left] != "?":
                maxLeft += int(num[left])
            else:
                leftNum += 1
            if num[right] != "?":
                maxRight += int(num[right])
            else:
                rightNum += 1
            left += 1
            right -= 1

        difNum = leftNum - rightNum
        if abs(difNum) == 1:
            return True
        if difNum > 0 and difNum % 2 == 0:
            maxLeft = maxLeft + 9 * difNum // 2
        elif difNum > 0 and difNum % 2 == 1:
            maxLeft = maxLeft + (9 * difNum // 2) + 9

        if difNum < 0 and abs(difNum):
            maxRight = maxRight + 9 * (abs(difNum) // 2)
        print(maxLeft, maxRight)
        return True if maxLeft != maxRight else False


if __name__ == "__main__":
    s = Solution()
    # print(s.sumGame("5023"))
    # print(s.sumGame("25??"))
    # print(s.sumGame("?3295???"))
    # print(s.sumGame("9?"))
    print(s.sumGame("8?6?90?5"))