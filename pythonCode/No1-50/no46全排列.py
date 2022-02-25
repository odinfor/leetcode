class Solution:
    def permute(self, nums: list) -> list:
        if not nums:
            return nums
        used = [False] * len(nums)
        res, path = [], []
        def dfs(nums, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    dfs(nums, used)
                    used[i] = False
                    path.pop()
        dfs(nums, used)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))
