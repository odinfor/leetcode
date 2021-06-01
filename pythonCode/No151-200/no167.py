class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        if len(numbers) < 2:
            return []
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
                continue
            if numbers[left] + numbers[right] > target:
                right -= 1
                continue

        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))