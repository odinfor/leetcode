#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        ans = 0
        left = 0
        while left < len(nums) - 1:
            right = len(nums) - 1
            while left < right:
                if nums[left] != nums[right]:
                    right -= 1
                    continue
                ans += 1
                right -= 1
            left += 1
        return ans
# @lc code=end

if __name__ == "__main__":
    print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
    print(Solution().numIdenticalPairs([1,1,1,1]))

