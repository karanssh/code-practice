package main

import (
	"fmt"
	"sort"
	"strconv"
)

func sortedSquares(nums []int) []int {
	for k, v := range nums {
		nums[k] = v * v
	}
	sort.Ints(nums)
	return nums
}
func findMaxConsecutiveOnes(nums []int) int {
	max := 0
	count := 0
	if len(nums) == 1 {
		return nums[0]
	}
	for i := 0; i < len(nums); i++ {
		if nums[i] == 1 {
			count++

		} else {
			// fmt.Printf("count %d \n", count)
			// fmt.Printf("max Ones %d \n", maxOnes)
			if max < count {
				max = count
			}
			count = 0
		}
	}
	if count >= max {
		max = count
	}
	return max
}
func findNumbers(nums []int) int {
	count := 0
	for _, v := range nums {
		val := strconv.Itoa(v)
		if len(val)%2 == 0 {
			count++
		}
	}
	return count

}
func duplicateZeros(arr []int) {
	fmt.Println("before insert", arr)
	count := 0
	for _, v := range arr {
		if v == 0 {
			count++
		}
	}
	arr2 := make([]int, len(arr)+count)
	k := 0
	for i := 0; i < len(arr2); i++ {
		arr2[i] = arr[k]
		if arr[k] == 0 {
			arr2[i+1] = 0
			i++
		}
		k++
	}
	arr = arr2
	fmt.Println("after insert", arr)
}
func insert(a []int, index int, value int) []int {
	arr := make([]int, 0)
	if len(a) == index+1 {
		return append(a, value)
	}
	arr = append(a[:index+1], value)
	arr = append(arr, a[index+1:]...)
	// a = append(a[:index+1], a[index:]...) // index < len(a)
	fmt.Println("array:", arr)
	// a[index+1] = value
	// fmt.Println("array after insert:", a)
	return arr
}

// func main() {
// 	arrayInput := []int{0}
// 	// arrayInput := []int{1, 0, 2, 3, 0, 4, 5, 0}
// 	duplicateZeros(arrayInput)
// 	// fmt.Println(arrayInput)
// 	// val := findNumbers([]int{1, 0, 2, 3, 0, 4, 5, 0})

// 	// fmt.Println("answer is ", val)
// }
