class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        # 双指针
        left, right = 0, len(nums) - 1
        left_index, right_index = -1, -1
        left_found, right_found = False, False

        while left <= right:
            if nums[left] == target and not left_found:
                left_index = left
                left_found = True
            if nums[right] == target and not right_found:
                right_index = right
                right_found = True
            
            if not left_found and not right_found:
                left += 1
                right -= 1
            elif left_found and not right_found:
                right -= 1
            elif not left_found and right_found:
                left += 1
            else:
                break

        return [left_index, right_index]



    
            
            