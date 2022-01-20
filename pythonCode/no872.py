#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 5:05 下午
# @Site    : 
# @File    : no872.py
# @desc    :

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res1, res2 = [], []

        self.__dfs(root1, res1)
        self.__dfs(root2, res2)

        return res1 == res2

    def __dfs(self, root: TreeNode, res: list):
        if root is None:
            return res

        if root.left is None and root.right is None:
            res.append(root.val)

        self.__dfs(root.left, res)
        self.__dfs(root.right, res)
