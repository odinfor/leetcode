#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 3:27 下午
# @Site    : 
# @File    : no680.py
# @desc    :
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s.l

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            sub_str = s[left:right + 1]
            # 尝试删除left判断余下子串是否是回文串
            sl, sr = 1, len(sub_str) - 1
            while sl < sr:
                if sub_str[sl] == sub_str[sr]:
                    sl += 1
                    sr -= 1
                else:
                    break
            if sl >= sr:
                return True

            # 尝试删除right判断余下子串是否是回文串
            sl, sr = 0, len(sub_str) - 2
            while sl < sr:
                if sub_str[sl] == sub_str[sr]:
                    sl += 1
                    sr -= 1
                else:
                    break
            if sl >= sr:
                return True

            return False

        return True


if __name__ == "__main__":
    s = Solution()
    # print(s.validPalindrome("abc"))
    # print(s.validPalindrome("abca"))
    # print(s.validPalindrome("aba"))
    # print(s.validPalindrome("abbaabab"))
    print(s.validPalindrome("cbbcc"))