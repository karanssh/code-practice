package main

import (
	"fmt"
	"io"
	"strconv"
)

func uniqueCharacters(str string) bool {

	// If at any time we encounter 2
	// same characters, return false
	for i := 0; i < len(str)-1; i++ {
		for j := i + 1; j < len(str); j++ {
			if str[i] == str[j] {
				return false
			}
		}
	}

	// If no duplicate characters encountered,
	// return true
	return true
}

func cf271a(in io.Reader, out io.Writer) {

	var n int
	fmt.Fscan(in, &n)
	nextYearInt := n + 1
	nextYear := strconv.Itoa(n + 1)
	for !uniqueCharacters(nextYear) {
		nextYearInt++
		nextYear = strconv.Itoa(nextYearInt)

	}
	fmt.Println(nextYearInt)
}

// func main() {

// 	// cf271a(os.Stdin, os.Stdout)

// }
