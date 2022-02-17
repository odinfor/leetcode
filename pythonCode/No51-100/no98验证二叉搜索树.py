#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 2:14 下午
# @Site    : 
# @File    : no98验证二叉搜索树.py
# @desc    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """递归"""
        def check(node: TreeNode, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            currVal = node.val
            if currVal <= lower or currVal >= upper:
                return False
            if not check(node.left, lower, currVal):
                return False
            if not check(node.right, currVal, upper):
                return False
            return True
        return check(root)


