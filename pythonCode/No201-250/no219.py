class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        # 将间隔k长度的作为一个窗口，没有超过k长度加入数据，超过则移除最先加入的元素。
        set_list = []
        for n in nums:
            if len(set_list) >= k + 1:
                set_list.pop(0)
            if n in set_list:
                return True
            else:
                set_list.append(n)

        return False

    def containsNearbyDuplicate2(self, nums: list, k: int) -> bool:
        # 使用哈希表方式
        nums_map = {}
        for i in range(len(nums)):
            if nums[i] not in nums_map:
                nums_map[nums[i]] = i
            else:
                diff_index = i - nums_map[nums[i]]
                if diff_index <= k:
                    return True
                else:
                    nums_map[nums[i]] = i

        return False

                
if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate2([1,2,3,1], 3))
    print(s.containsNearbyDuplicate2([1,2,3,1,2,3], 2))