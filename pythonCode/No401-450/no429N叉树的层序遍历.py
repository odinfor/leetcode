#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 5:23 下午
# @Site    : 
# @File    : no429N叉树的层序遍历.py
# @desc    :


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> list:
        if not root:
            return []

        ans = list()
        q = deque([root])

        while q:
            cnt = len(q)
            level = list()
            for _ in range(cnt):
                cur = q.popleft()
                level.append(cur.val)
                for child in cur.children:
                    q.append(child)
            ans.append(level)

        return ans

