#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 5:28 下午
# @Site    : 
# @File    : no1791.py
# @desc    :

class Solution:
    def findCenter(self, edges: list) -> int:
        node = {}
        for i in edges:
            if node.get(i[0]):
                node[i[0]] += 1
            else:
                node[i[0]] = 1
            if node.get(i[1]):
                node[i[1]] += 1
            else:
                node[i[1]] = 1

        for k, v in node.items():
            if v == len(edges):
                return k

