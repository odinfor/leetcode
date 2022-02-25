class Solution:
    def lemonadeChange(self, bills: list) -> bool:
        fiveNum, tenNum, twenNum = 0, 0, 0
        for i in bills:
            if i == 5:
                fiveNum += 1
            elif i == 10:
                fiveNum -= 1
                tenNum += 1
            elif i == 20:
                if tenNum:
                    tenNum -= 1
                    fiveNum -= 1
                else:
                    fiveNum -= 3
            if fiveNum < 0 or tenNum < 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.lemonadeChange([5,5,5,10,5,5,10,20,20,20]))