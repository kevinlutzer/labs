package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func makeList(nums []int) *ListNode {
	var l *ListNode = nil
	for i := len(nums) - 1; i >= 0; i-- {
		nl := &ListNode{Val: nums[i], Next: l}
		l = nl
	}

	return l
}

func printListNode(l *ListNode) {
	if l == nil {
		return
	}

	fmt.Printf("%d", l.Val)
	printListNode(l.Next)
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var nl *ListNode
	var first *ListNode

	l2val := 0
	l1val := 0
	c := 0

	for l1 != nil && l2 != nil {
		if l1 != nil {
			l1val = l1.Val
		}

		if l2 != nil {
			l2val = l2.Val
		}

		fmt.Printf("l1, l2: %d, %d", l1val, l2val)

		v := l2val + l1val + c

		c = 0
		if v >= 10 {
			v = v - 10
			c = 1
		}

		fmt.Printf("Result: %d\n", v)

		nl = &ListNode{Val: v, Next: nl}

		if first == nil {
			first = nl
		}

		if l1 != nil {
			l1 = l1.Next
		}

		if l2 != nil {
			l2 = l2.Next
		}
	}

	return first
}

func main() {
	// f := makeList([]int{0, 1, 2, 3, 4})
	// s := makeList(([]int{9, 8, 4, 8, 3}))
	f := makeList([]int{2, 4, 3})
	s := makeList(([]int{5, 6, 4}))

	nl := addTwoNumbers(f, s)
	printListNode(nl)
}
