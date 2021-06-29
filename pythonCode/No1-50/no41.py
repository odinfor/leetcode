class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        """
        数组元素不重复，理想排序状态为 [1, 2, 3, 4, 5, 6, 7],由于空间要求为O(1)不能使用额外的hash方法。
        理想排序下即元素value == 元素的索引+1.需要修改原数组的方式实现
        思路是遍历数组，将nums[i] != i + 1且nums[i]为整数且不大于n，另外 nums[i] != nums[nums[i] - 1]的两个元素位置互换。
        类似桶排序思路
        不满足上述条件则跳过，最后遍历修改后的数组返回对应位置上不正确的数
        """
        if not nums:
            return 1

        nums_len = len(nums)
        for i in range(nums_len):
            while 0 < nums[i] <= nums_len and nums[i] != nums[nums[i] - 1]:
                nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        print(nums)
        for i in range(nums_len):
            if nums[i] != i + 1:
                return i + 1

        return nums_len + 1


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([3, 4, -1, 1]))
    # print(s.firstMissingPositive([7,8,9,11,12]))
    # print(s.firstMissingPositive([-1,-2,-60,40,43]))