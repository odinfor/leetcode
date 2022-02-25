class Solution:
    def wiggleMaxLength(self, nums: list) -> int:
        n = len(nums)
        if n < 2:
            return n

        startDiff = nums[1] - nums[0]
        res = (2 if startDiff != 0 else 1)
        for i in range(2, n):
            currDiff = nums[i] - nums[i - 1]
            if (currDiff > 0 and startDiff <= 0) or (currDiff < 0 and startDiff >= 0):
                res += 1
                startDiff = currDiff

        return res


if __name__ == "__main__":
    s = Solution()
    # print(s.wiggleMaxLength([1,7,4,9,2,5]))
    print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
