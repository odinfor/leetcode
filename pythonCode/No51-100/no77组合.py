
class Solution:
    def combine(self, n: int, k: int) -> list:

        used = [False] * n  # 记录用过的值,用于剪枝
        nums = [1 + x for x in range(n)]
        res = []

        def dfs(nums, path: list, res: list, used, deep, size):
            if deep == size:    # 结束条件
                res.append(path.copy())
                return
            for i in range(n):
                # 横向遍历
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    dfs(nums, path, res, used, deep + 1, size)  # 纵向遍历,递归过程
                    # 回退操作
                    used[i] = False
                    path.pop()

        dfs(nums, [], res, used, 0, k)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))