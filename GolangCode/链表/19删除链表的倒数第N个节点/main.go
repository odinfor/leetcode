package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	prev := &ListNode{
		Val:  0,
		Next: head,
	}
	startNode := prev.Next
	endNode := head
	for i := 0; i < n; i++ {
		endNode = endNode.Next
	}
	for currNode := endNode; currNode != nil; currNode = currNode.Next {
		startNode = startNode.Next
	}
	startNode.Next = startNode.Next.Next
	return prev.Next
}
