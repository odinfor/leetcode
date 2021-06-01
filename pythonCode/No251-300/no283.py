class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or not nums:
            return

        for left in range(len(nums) - 1):
            if nums[left] != 0:
                continue
            for right in range(left + 1, len(nums)):
                if nums[right] == 0:
                    continue
                nums[left], nums[right] = nums[right], nums[left]
                break

        print(nums)


if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([0,1,0,3,12])