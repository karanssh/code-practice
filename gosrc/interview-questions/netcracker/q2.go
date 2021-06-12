package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println("Hi Friend!")
}

func sortArray(a []int) []int {
	sort.Ints(a)
	return a
}
