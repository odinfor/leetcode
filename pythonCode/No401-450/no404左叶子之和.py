#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 10:58 上午
# @Site    : 
# @File    : no404左叶子之和.py
# @desc    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """BFS"""
        if not root:
            return 0
        inQueue = list()
        res = 0
        # 根节点压入
        inQueue.append(root)
        while inQueue:
            temp = inQueue[0]
            if temp.left:
                inQueue.append(temp.left)
                if not temp.left.left and not temp.left.right:
                    res += temp.left.val
            if temp.right:
                inQueue.append(temp.right)
            inQueue.pop(0)  # temp弹出压入队列

        return res
