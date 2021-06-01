class Solution:
    def majorityElement(self, nums: list) -> int:
        # 根据二分之一原则，排序过后超过一半的元素一定会在中间
        nums.sort()
        return nums[len(nums)//2]