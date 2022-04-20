package main

import (
	"fmt"
)

func shortestToChar(s string, c byte) []int {
	var (
		idxList = make([]int, 0)
		res     = make([]int, 0)
		left    = 0
		right   = 1
	)
	for i := 0; i < len(s); i++ {
		if s[i] != c {
			continue
		}
		idxList = append(idxList, i)
	}
	if len(idxList) == 1 {
		for i := 0; i < len(s); i++ {
			if i < idxList[0] {
				res = append(res, idxList[0]-i)
			} else if i == idxList[0] {
				res = append(res, 0)
			} else {
				res = append(res, i-idxList[0])
			}
		}
		return res
	}
	for i := 0; i < len(s); i++ {
		if left == 0 && i < idxList[left] {
			res = append(res, idxList[left]-i)
		} else if i == idxList[left] {
			res = append(res, 0)
		} else if {

		}
	}

	return res
}

func main() {
	res1 := shortestToChar("loveleetcode", 'e')
	res2 := shortestToChar("aaab", 'b')
	res3 := shortestToChar("aaba", 'b')
	fmt.Println(res1, res2, res3)
}
