#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 6:03 下午
# @Site    : 
# @File    : no101.py
# @desc    :

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.checkNode(root, root)

    def checkNode(self, node1: TreeNode, node2: TreeNode) -> bool:
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False

        return node1.val == node2.val and self.checkNode(node1.left, node2.right) and self.checkNode(node1.right, node2.left)
