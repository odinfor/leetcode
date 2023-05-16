#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(newS) - 1
        while left < right:
            if newS[left] != newS[right]:
                return False
            left += 1
            right -= 1
        return True
# @lc code=end

