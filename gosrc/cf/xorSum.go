package main

import "fmt"

func main() {
	a := 5
	b := 5
	if xorSum(a, b) == 10 {
		fmt.Println("pass")
	} else {
		fmt.Println("fail")

	}
}
func xorSum(a, b int) int {
	xorSum := 0
	for b != 0 {
		xorSum = a ^ b
		b = a & b
		b = b << 1
		a = xorSum
	}
	return a
}
