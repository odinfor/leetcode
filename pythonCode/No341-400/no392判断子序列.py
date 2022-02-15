#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 4:35 下午
# @Site    : 
# @File    : no392判断子序列.py
# @desc    : 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#            字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx, s_len, res = 0, len(s), False
        for i in range(len(t)):
            if t[i] == s[s_idx]:
                s_idx += 1
                if s_idx == s_len:
                    res = True
                    break

        return res

    """
    思路及算法

考虑前面的双指针的做法，我们注意到我们有大量的时间用于在 tt 中找到下一个匹配字符。

这样我们可以预处理出对于 tt 的每一个位置，从该位置开始往后每一个字符第一次出现的位置。

我们可以使用动态规划的方法实现预处理，令 f[i][j]f[i][j] 表示字符串 tt 中从位置 ii 开始往后字符 jj 第一次出现的位置。在进行状态转移时，如果 tt 中位置 ii 的字符就是 jj，那么 f[i][j]=if[i][j]=i，否则 jj 出现在位置 i+1i+1 开始往后，即 f[i][j]=f[i+1][j]f[i][j]=f[i+1][j]，因此我们要倒过来进行动态规划，从后往前枚举 ii。

这样我们可以写出状态转移方程：

假定下标从 00 开始，那么 f[i][j]f[i][j] 中有 0 \leq i \leq m-10≤i≤m−1 ，对于边界状态 f[m-1][..]f[m−1][..]，我们置 f[m][..]f[m][..] 为 mm，让 f[m-1][..]f[m−1][..] 正常进行转移。这样如果 f[i][j]=mf[i][j]=m，则表示从位置 ii 开始往后不存在字符 jj。

这样，我们可以利用 ff 数组，每次 O(1)O(1) 地跳转到下一个位置，直到位置变为 mm 或 ss 中的每一个字符都匹配成功。

    """


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))