class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        start, total = 0, 0
        while start <= len(flowerbed) - 1:
            if start == 0 and flowerbed[start+1] == 0 and flowerbed[start] == 0:
                total += 1
            if start == len(flowerbed) - 1 and flowerbed[start - 1] == 0 and flowerbed[start] == 0:
                total += 1
            if 0 < start < len(flowerbed) - 1 and flowerbed[start - 1] == 0 and flowerbed[start + 1] == 0:
                total += 1
            start += 1

        return True if total > n else False


if __name__ == "__main__":
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1], 1))
    print(s.canPlaceFlowers([1,0,0,0,1], 2))