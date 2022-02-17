#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/16 4:05 下午
# @Site    : 
# @File    : no113路径总和2.py
# @desc    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list:
        """DFS"""
        allPath, path = list(), list()

        def dfs(root: TreeNode, targetSum: int):
            if not root:
                return
            path.append(root.val)
            targetSum -= root.val
            if targetSum == 0 and not root.left and not root.right:
                allPath.append(path[:])     # 这里要append path的值，append(path) 会由于path.pop()导致allPath中元素均为空列表
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()

        dfs(root, targetSum)
        return allPath


