class Solution:
    def arrayPairSum(self, nums: list) -> int:
        nums.sort()
        
        return sum(nums[::2])


if __name__ == "__main__":
    s = Solution()
    print(s.arrayPairSum([6, 2, 6, 5, 1, 2]))