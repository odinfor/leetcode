class Solution:
    def missingNumber(self, nums: list) -> int:
        if len(nums) == 1 and nums[0] == 0:
            return 1
        if len(nums) == 1 and nums[0] == 1:
            return 0

        nums.sort()
        for i in range(len(nums) + 1):
            if i < len(nums) and nums[i] != i:
                return i
            if i == len(nums):
                return len(nums)
            
        return None

if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3,0,1]))
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
    print(s.missingNumber([0]))
    print(s.missingNumber([0, 1]))