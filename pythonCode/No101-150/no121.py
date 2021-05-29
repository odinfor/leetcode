class Solution:
    def maxProfit(self, prices:list) -> int:
        if not list or len(prices) == 1:
            return 0
        buy_day, sale_day, max_price = 0, 0, 0

        for left in range(len(prices) - 1):
            if left != 0 and prices[left] > prices[left - 1]:
                continue
            for right in range(left + 1, len(prices)):
                if prices[left] >= prices[right]:
                    break
                else:
                    diff_price = prices[right] - prices[left]
                    if diff_price > max_price:
                        max_price, buy_day, sale_day = diff_price, left, right
        print(buy_day, sale_day)
        return max_price

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([2,1,2,1,0,1,2]))

                
        
