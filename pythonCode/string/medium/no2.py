class Solution:
    def removeElement(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1

        if target < nums[0]:
            return 0
        if target > nums[right]:
            return right + 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        return left

    
if __name__ == "__main__":
    s = Solution()
    # print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    print(s.removeElement([1,3,5,6], 3))
    print(s.removeElement([1,3,5,6], 2))
    print(s.removeElement([1,3,5,6], 0))
    print(s.removeElement([1,3,5,6], 5))

