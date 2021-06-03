class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums3 = nums1 + nums2
        if not nums3:
            return 0 / 1.0
        if len(nums3) == 1:
            return nums3[0] / 1.0
        nums3.sort()
        
        nums_len = len(nums3)
        if nums_len % 2 > 0:
            return nums3[nums_len // 2]
        else:
            mid = nums_len // 2
            return (nums3[mid] + nums3[mid - 1]) / 2.0


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,3], [2]))
    print(s.findMedianSortedArrays([1,2], [3, 4]))
    print(s.findMedianSortedArrays([0, 0], [0, 0]))
    print(s.findMedianSortedArrays([], [1]))