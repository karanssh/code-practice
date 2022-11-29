package main

import (
	"fmt"
	"io"
	"math"
)

func uniqueChafracters(str string) bool {

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

func gcd(a int, b int) int {
	if a == 0 {
		return b
	}
	return gcd(b%a, a)
}

func noOfCommonDivisors(in io.Reader, out io.Writer) {

	var a, b int
	fmt.Fscan(in, &a, &b)
	gcdValue := gcd(a, b)
	var total int
	for i := 1; i <= int(math.Round(math.Sqrt(float64(gcdValue)))); i++ {
		if gcdValue%i == 0 {
			// check if divisors are equal
			if gcdValue/i == i {
				total = total + 1
			} else {
				total = total + 2
			}
		}
	}
	fmt.Println(total)
}

// func main() { noOfCommonDivisors(os.Stdin, os.Stdout) }
