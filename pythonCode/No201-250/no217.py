class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        num_map = {}
        for n in nums:
            if n not in num_map:
                num_map[n] = 0
            else:
                return True

        return False