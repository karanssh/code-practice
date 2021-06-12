package main

import "fmt"

//partially done
func plusOne(digits []int) []int {

	reqValue := 0
	size := len(digits)

	for i := 0; i <= size-1; i++ {
		reqValue = reqValue*10 + digits[i]
	}
	fmt.Println(reqValue)
	reqValue++
	newArr := make([]int, 0)
	for reqValue > 0 {
		modVal := reqValue % 10
		newArr = append(newArr, modVal)
		reqValue = reqValue / 10
	}
	for i, j := 0, len(newArr)-1; i < j; i, j = i+1, j-1 {
		newArr[i], newArr[j] = newArr[j], newArr[i]
	}
	return newArr
}

// func main() {
// 	fmt.Println(plusOne([]int{0}))
// }
