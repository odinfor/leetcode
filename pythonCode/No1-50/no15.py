"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

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
            if start_index > 0 and nums[start_index] == nums[start_index - 1]: continue
            lr_sum = 0 - nums[start_index]  # 左右指针两数之和的预期值
            while left < right:
                if nums[left] + nums[right] > lr_sum:
                    right -= 1
                    continue
                if nums[left] + nums[right] < lr_sum:
                    left += 1
                    continue
                if nums[left] + nums[right] == lr_sum:
                    curr_list = [nums[start_index], nums[left], nums[right]]
                    if curr_list not in rst:
                        rst.append(curr_list)
                    left += 1

        return rst