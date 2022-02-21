package main

/*
暴力解法,使用两个map存放s，t内元素个数.
对比两个map中元素出现的次数
*/
func isAnagram(s string, t string) bool {
	sMap := make(map[int32]int)
	tMap := make(map[int32]int)
	if len(s) != len(t) {
		return false
	}
	for _, v := range s {
		if _, ok := sMap[v]; ok {
			sMap[v] += 1
		} else {
			sMap[v] = 1
		}
	}
	for _, v := range s {
		if _, ok := tMap[v]; ok {
			tMap[v] += 1
		} else {
			tMap[v] = 1
		}
	}
	for k, sv := range sMap {
		tv, ok := tMap[k]
		if !ok || tv != sv {
			return false
		}
	}
	return true
}
