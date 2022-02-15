#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/8 5:20 下午
# @Site    : 
# @File    : 39组合总和.py
# @desc    : 给你一个 无重复元素 的整数数组candidates 和一个目标整数target，找出candidates中可以使数字和为目标数target 的 所有不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
#            candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
#            对于给定的输入，保证和为target 的不同组合数少于 150 个。

class Solution:
    def dfs(self, candidates, begin, size, path, res, target):
        """
        回溯递归方法，避免重复需要剪枝。每一枝使用begin记录当前index位置从后回溯
        回溯结束条件：target <= 0 & begin < len(candidates)
        """
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(begin, size):
            self.dfs(candidates, i, size, path + [candidates[i]], res, target - candidates[i])

    def combinationSum(self, candidates: list, target: int) -> list:
        """回溯"""

        size = len(candidates)
        if size == 0:
            return []
        path, res = [], []
        self.dfs(candidates, 0, size, path, res, target)

        return res
