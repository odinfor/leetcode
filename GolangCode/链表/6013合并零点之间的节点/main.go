package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeNodes(head *ListNode) *ListNode {
	prev := &ListNode{
		Val:  0,
		Next: head,
	}
	start := prev
	currSum := 0
	for curr := head; curr.Next != nil; curr = curr.Next {
		if curr.Next.Val != 0 {
			currSum += curr.Val
		} else {
			curr.Val = currSum + curr.Val
			start.Next = curr
			start = start.Next
			currSum = 0
		}
	}
	start.Next = nil
	return prev.Next
}
