"""
给你一个整数数组 nums 和一个整数 k 。请你向 nums 中追加 k 个 未 出现在 nums 中的、互不相同 的 正 整数，并使结果数组的元素和 最小 。
返回追加到 nums 中的 k 个整数之和。

示例1
输入：nums = [1,4,25,10,25], k = 2
输出：5
解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 2 和 3 。
nums 最终元素和为 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70 ，这是所有情况中的最小值。
所以追加到数组中的两个整数之和是 2 + 3 = 5 ，所以返回 5 。

示例2
输入：nums = [5,6], k = 6
输出：25
解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 1 、2 、3 、4 、7 和 8 。
nums 最终元素和为 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36 ，这是所有情况中的最小值。
所以追加到数组中的两个整数之和是 1 + 2 + 3 + 4 + 7 + 8 = 25 ，所以返回 25 。
"""


class Solution:
    def __getSum(self, a1, an, n) -> int:   # 等差数列求和
        return int(n * (a1 + an) / 2) if n > 1 else a1

    def minimalKSum(self, nums: list, k: int) -> int:
        """
        对nums排序后滑动窗口插入
        """
        baseNum, currSum = 1, 0
        nums.sort()
        if not nums:
            return 0

        # 如果nums只有一个元素
        if len(nums) == 1:
            if nums[0] == 1:
                return self.__getSum(2, k + 1, k)
            elif nums[0] > k:
                return self.__getSum(1, k, k)
            else:
                return self.__getSum(1, k + 1, k + 1) - nums[0]

        # 如果nums是递增
        if nums[-1] - nums[0] == len(nums) - 1:
            leftNum = nums[0] - 1
            rightNum = k - leftNum
            return self.__getSum(1, leftNum, leftNum) + self.__getSum(nums[-1] + 1, nums[-1] + rightNum, rightNum)

        # nums起始点左侧可以插入的元素个数
        leftAddNum = nums[0] - baseNum
        if leftAddNum >= k:
            return self.__getSum(1, k, k)
        currSum = self.__getSum(1, leftAddNum, leftAddNum)
        k -= leftAddNum

        # 开始滑动
        left, right = 0, 1
        while right < len(nums):
            if nums[right] - nums[left] <= 1:
                left += 1
                right += 1
                continue
            # 可以插入的个数
            if k > nums[right] - nums[left] - 1:
                currSum += self.__getSum(nums[left] + 1, nums[right] - 1, nums[right] - nums[left] - 1)
                k -= nums[right] - nums[left] - 1
                left += 1
                right += 1
            else:
                return currSum + self.__getSum(nums[left] + 1, nums[left] + k, k)

        # 剩下的可插入数量
        return currSum + self.__getSum(nums[-1] + 1, nums[-1] + k, k)


if __name__ == '__main__':
    m = Solution()
    # print(m.minimalKSum2([5, 6], 6))
    # print(m.minimalKSum2([53,41,90,33,84,26,50,32,63,47,66,43,29,88,71,28,83], 76))
    print(m.minimalKSum([96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84], 35))
    print(m.minimalKSum([3], 1))
    print(m.minimalKSum([904], 98022370))
    print(m.minimalKSum([2], 5))
