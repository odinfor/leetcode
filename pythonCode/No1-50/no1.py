class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    """

    @staticmethod
    def two_sum1(target: int, nums: list) -> list:
        # 遍历破解
        for num in nums:
            left_num, new_list = target - num, nums[nums.index(num) + 1:]
            if left_num in new_list:
                return [nums.index(num), nums.index(num) + new_list.index(left_num) + 1]

    @staticmethod
    def two_sum2(target: int, nums: list) -> list:
        # 使用hash
        create_dict = dict(zip(range(len(nums)), nums))

        for i in range(len(nums)):
            if i == len(nums) - 1:
                return []
            y = i + 1
            while y < len(nums):
                if create_dict[i] + create_dict[y] == target:
                    return [i, y]
                y += 1

    @staticmethod
    def two_sum3(target: int, nums: list) -> list:
        # 使用hash记录,以列表的值: 索引的形式.
        diff_dict = {}      # 创建map
        for k, v in enumerate(nums):    # 遍历列表的index&value
            diff = target - v

            if diff in diff_dict:
                return [diff_dict.get(diff), k]

            diff_dict[v] = k


if __name__ == "__main__":
    s = Solution()
    print(s.two_sum1(9, [2, 7, 11, 15]))
    print(s.two_sum1(6, [3, 2, 4]))
    print(s.two_sum1(6, [3, 3]))

    print(s.two_sum2(9, [2, 7, 11, 15]))
    print(s.two_sum2(6, [3, 2, 4]))
    print(s.two_sum2(6, [3, 3]))


