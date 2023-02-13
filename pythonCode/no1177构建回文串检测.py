#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/21 10:43 上午
# @Site    : 
# @File    : no1177构建回文串检测.py
# @desc    :

class Solution:
    def canMakePaliQueries(self, s: str, queries: list) -> list:
        if not s:
            return [False]
        if len(s) == 1:
            return [True]
        res = []
        for q in queries:
            left, right, count, q_map, q_val = q[0], q[1], q[2], dict(), 0
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    continue
                if q_map.get(s[left]):
                    q_map[s[left]] -= 1
                else:
                    q_map[s[left]] = 1
                if q_map.get(s[right]):
                    q_map[s[right]] -= 1
                else:
                    q_map[s[right]] = 1
                left += 1
                right -= 1
            for _, v in q_map.items():
                q_val += v
            if q_val <= 2 * count + 1:
                res.append(True)
            else:
                res.append(False)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.canMakePaliQueries("abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
    print(s.canMakePaliQueries("hunu", [[0, 3, 1]]))


