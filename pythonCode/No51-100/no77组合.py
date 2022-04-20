
class Solution:
    def combine(self, n: int, k: int) -> list:

        used = [False] * n  # 记录用过的值,用于剪枝
        nums = [1 + x for x in range(n)]
        res = []

        def dfs(nums, path: list, res: list, used, deep, size):
            if len(path) == k:    # 结束条件
                res.append(path.copy())
                return
            for i in range(deep, len(nums)):
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

    def combine2(self, n: int, k: int) -> list:
        res = []    #存放符合条件结果的集合
        path = []   #用来存放符合条件结果

        def backtrack(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex, n-(k-len(path))+2):  #优化的地方
                path.append(i)  #处理节点
                backtrack(n, k, i+1)  #递归
                path.pop()  #回溯，撤销处理的节点
        backtrack(n, k, 1)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))