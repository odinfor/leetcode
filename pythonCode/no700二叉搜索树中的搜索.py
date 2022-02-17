#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 4:00 下午
# @Site    : 
# @File    : no700二叉搜索树中的搜索.py
# @desc    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        while curr:
            if curr.val < val:
                curr = curr.right
            elif curr.val > val:
                curr = curr.left
            else:
                return curr
        return

