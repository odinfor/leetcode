#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 10:12 上午
# @Site    : 
# @File    : no226.py
# @desc    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        # 交换当前节点左右子树
        root.left, root.right = root.right, root.left
        # 递归交换所有左右子树节点
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

