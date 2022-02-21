#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/18 9:48 上午
# @Site    : 
# @File    : no236二叉树的最近公共祖先.py
# @desc    :

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        leftRoot, rightRoot = root.left, root.right
        if (p == leftRoot and q == rightRoot) or (p == rightRoot and q == leftRoot):
            return root
        deep_p, deep_q = 1, 1
        leftQueue = []
        leftQueue.append(leftRoot)
        while leftQueue:
            temp = leftQueue[0]
            if temp.left:

