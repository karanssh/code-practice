package main

import (
	"fmt"
	"sort"
)

/*
given an array find triplet such that their sum is 0.

[ 5, -4, -1, 2, 3, 9 ]

output: 5, -4, -1

*/

/*

abbaca remove consecutive alphabets

abbaca
aaca
ca

so we remove bb : aaca

ac

condition of removal is, i, j is removed is i = j+1 and s[i] = s[j]

*/

func main() {
	testData := []int{5, -4, -1, 2, 3, 9}
	sort.Ints(testData)
	outputData := foo(0, testData)

	fmt.Println("got output data as: ", outputData)
}

func foo(targetSum int, arr []int) []int {

	initialSum := 0
	for i := 2; i < len(arr); i++ {
		fmt.Println("matched : ", arr[i], arr[i-1], arr[i-2])
		initialSum = arr[i] + arr[i-1] + arr[i-2]
		fmt.Println("init sum is : ", initialSum)
		if initialSum == targetSum {
			//return the three values that I put in initial sum
			fmt.Println("matched : ", arr[i], arr[i-1], arr[i-2])
			return []int{arr[i], arr[i-1], arr[i-2]}
		}
	}
	return []int{}
}

func foo2(targetSum int, arr []int) {
	var windowStart int = 0
	var minSumInt int = -9999
	var windowSum int = 0
	for windowEnd := 0; windowEnd < len(arr); windowEnd++ {
		windowSum = windowSum + arr[windowEnd] // -2 -1 8 9 10

		for windowSum >= targetSum {
			if minSumInt > windowEnd-windowStart+1 {
				minSumInt = 2 //something goes here, need to think
			} else {
				minSumInt = windowEnd - windowStart + 1
			}
			windowSum = windowSum - arr[windowStart]

		}
	}
}
