class Solution:
    def search(self, nums: list, target: int) -> int:
        if not nums:
            return -1
        elif len(nums) == 1 and target in nums:
            return 0
        elif len(nums) == 1 and target not in nums:
            return -1
            
        nums_len = len(nums)
        left, rigth = 0, nums_len - 1

        while left <= rigth:
            mid = (rigth - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    rigth = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[rigth]:
                    left = mid + 1
                else:
                    rigth = mid - 1

        return -1

