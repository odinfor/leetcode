class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        min_sum, min_value = 999999, 999999

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                curr_value = abs(curr_sum - target)
                if curr_value  < min_value:
                    min_value, min_sum = curr_value, curr_sum

                if curr_sum < target:
                    left += 1
                    continue
                elif curr_sum > target:
                    right -= 1
                    continue
                else:
                    return curr_sum

        return min_sum



if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([1, 1, 1, 0], -100))
    print(s.threeSumClosest([0,2,1,-3], 1))
    print(s.threeSumClosest([0, 1, 2], 3))