#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 5:59 下午
# @Site    : 
# @File    : no112.py
# @desc    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """DFS"""
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)