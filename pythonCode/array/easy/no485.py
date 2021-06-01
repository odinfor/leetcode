class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        # 滑动窗口
        left, right, max_len = 0, 0, 0
        if not nums:
            return 0
        if len(nums) == 1 and nums[0] == 1:
            return 1
        if len(nums) == 1 and nums[0] != 1:
            return 0

        while right < len(nums):
            if nums[right] != 0:
                right += 1
            else:
                right += 1
                left = right
            max_len = max(max_len, right - left)

        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))
    print(s.findMaxConsecutiveOnes([0, 1]))