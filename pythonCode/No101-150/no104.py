#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 5:49 下午
# @Site    : 
# @File    : no104.py
# @desc    :

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_deep = self.maxDepth(root.left)
        right_deep = self.maxDepth(root.right)

        return max(left_deep, right_deep) + 1
