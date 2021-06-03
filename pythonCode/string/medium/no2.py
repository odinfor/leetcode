class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        rst = []

        if len(nums) < 3:
            return []
        if nums[0] > 0 or nums[-1] < 0:
            return []

        for start_index in range(len(nums) - 2):
            left, right = start_index + 1, len(nums) - 1
            # if nums[start_index] == nums[start_index + 1]: continue
            lr_sum = 0 - nums[start_index]  # 左右指针两数之和的预期值
            while left < right:
                if nums[left] + nums[right] > lr_sum:
                    right -= 1
                    continue
                if nums[left] + nums[right] < lr_sum:
                    left += 1
                    continue
                if nums[left] + nums[right] == lr_sum: 
                    rst.append([nums[start_index], nums[left], nums[right]])
                    left += 1

        return rst
            

    
if __name__ == "__main__":
    s = Solution()
    # print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))

