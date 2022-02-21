package main

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		_, ok := numMap[nums[i]]
		if ok {
			res := []int{numMap[nums[i]], nums[i]}
			return res
		}
		numMap[target-nums[i]] = i
	}
	return nil
}
