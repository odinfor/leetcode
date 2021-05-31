class Solution:
    def maxProfit(self, prices: list) -> int:
        # 差值问题，收益最大转换为前后两两差值为正的总和
        start, max_value = 0, 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            max_value = max_value + tmp if tmp > 0 else max_value
        
        return max_value


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))