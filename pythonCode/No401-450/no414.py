class Solution:
    def thirdMax(self, nums: list) -> int:
        nums_set = set(nums)
        new_set = sorted(nums_set)
        new_list = list(new_set)
        
        return new_list[-1] if len(new_list) < 3 else new_list[-3]


if __name__ == "__main__":
    s = Solution()
    # print(s.thirdMax([3, 2, 1]))
    # print(s.thirdMax([1, 2]))
    # print(s.thirdMax([2, 2, 3, 1]))
    print(s.thirdMax([-1, -2,2,3]))