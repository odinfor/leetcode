#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/8 6:43 下午
# @Site    : 
# @File    : 98.py
# @desc    :

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(root: TreeNode):
            if not root.left or not root.right:
                return True

            if (not root.left and root.right) or (root.left and not root.right):
                return False
            if root.left.val >= root.val or root.right.val <= root.val:
                return False

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return True

