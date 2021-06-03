class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        nums_map, mis_list = {}, []
        for n in nums:
            nums_map[n] = 0
        
        for i in range(1, len(nums) + 1):
            if i not in nums_map:
                mis_list.append(i)

        return mis_list

        