package main

import (
	"fmt"
	"sort"
)

//linked list

// 1->2 ->3 ->4 ->5 pairwise swap

/*

1 ->  2 -> 3 ->4 ->$
-> 0x01  0x0a 0x0b -> nil

2 ->  1 -> 3 ->4 ->$
0x0a  0x01 0x0b
2 ->1 ->3

2 ->1 -> 4 ->3 ->5
*/

type Node struct {
	Value int
	Next  *Node
}

func main() {
	testData := []int{5, -4, -1, 2, 3, 9}
	sort.Ints(testData)
	pairSwap(nil, head)

	fmt.Println("got output data as: ", outputData)
}

func pairSwap(prev, head *Node) {
	nextNode := head.Next
	if nextNode == nil {
		return
	}
	swap(*head, *head.Next)
	//head
	if head.Next == nil {

	}
	head.Next = prev.Next
	//head.Next
	prev.Next = head.Next
	head.Value = nextNode.Value
	p

}
