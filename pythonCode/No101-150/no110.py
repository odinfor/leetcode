#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 5:56 下午
# @Site    : 
# @File    : no110.py
# @desc    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.deep(root) != -1

    def deep(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.deep(root.left)
        if left == -1:
            return -1
        right = self.deep(root.right)
        if right == -1:
            return -1

        return max(left, right) + 1 if abs(left - right) < 2 else -1

