#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/16 3:07 下午
# @Site    : 
# @File    : baseFunc.py
# @desc    :

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"


class ListToTree(object):

    def __init__(self, nums: list):
        self.nums = nums
        self.queue = []
        if len(nums) == 1:
            self.root = TreeNode(self.nums.pop(0))
        else:
            a = self.nums.pop(0)
            b = self.nums.pop(0)
            c = self.nums.pop(0)
            self.root = TreeNode(a)
            if b is not None:
                self.root.left = TreeNode(b)
            else:
                self.root.left = b
            if c is not None:
                self.root.right = TreeNode(c)
            else:
                self.root.right = c
            self.queue.append(self.root.left)
            self.queue.append(self.root.right)

    def main(self):
        while len(self.nums) > 0 and len(self.queue)> 0:
            node = self.queue.pop(0)
            if node is not None:
                num= self.nums.pop(0)
                if num is not None:
                    node.left = TreeNode(num)
                else:
                    node.left = num
                num = self.nums.pop(0)
                if num is not None:
                    node.right = TreeNode(num)
                else:
                    node.right = num
                self.queue.append(node.left)
                self.queue.append(node.right)
        return self.root


if __name__ == "__main__":
    t = ListToTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    print(t.main())