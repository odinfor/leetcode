#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 5:41 下午
# @Site    : 
# @File    : no844比较含退格的字符串.py
# @desc    :

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS, stackT = [], []
        for i in s:
            if not stackS and i == "#":
                continue
            if stackS and i == "#":
                stackS.pop(-1)
                continue
            stackS.append(i)
        for i in t:
            if not stackT and i == "#":
                continue
            if i == "#" and stackT:
                stackT.pop(-1)
                continue
            stackT.append(i)

        return True if stackS == stackT else False


if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare("ab#c", "ad#c"))