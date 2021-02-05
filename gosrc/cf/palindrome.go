package main

import (
	"fmt"
	"regexp"
	"strings"
)

func main() {
	input := "A man, a plan, a canal: Panama"
	if isPalindromeIgnoreCase(input) {
		fmt.Println("pass")
	} else {
		fmt.Println("fail")

	}
}
func isPalindromeIgnoreCase(input string) bool {
	reg := regexp.MustCompile("[^a-zA-Z0-9 *]")
	reg2 := regexp.MustCompile("\\s")
	dat := reg.ReplaceAll([]byte(input), nil)
	dat = reg2.ReplaceAll(dat, nil)
	fmt.Println(string(dat))
	input = strings.ToLower(string(dat))
	for i := 0; i < len(input)/2; i++ {
		if input[i] != input[len(input)-i-1] {
			return false
		}
	}
	return true

}

/*ListNode isDefinition for singly-linked list.
 *
 *
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	l3 := &ListNode{}
	for {
		if l1 == nil {
			l3.Next = l2.Next
			break
		} else if l2 == nil {
			l3.Next = l1.Next
			break
		}
		if l1.Val <= l2.Val {
			l3.Val = l1.Val
			l1 = l1.Next
		} else {
			l3.Val = l2.Val
			l2 = l2.Next
		}
		l3 = l3.Next
	}
	return l3
}
