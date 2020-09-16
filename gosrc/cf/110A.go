package main

import (
	"fmt"
	"io"
)

func cf110a(in io.Reader, out io.Writer) {
	var n int
	var arr [10]int
	fmt.Fscan(in, &n)
	for n != 0 {
		arr[n%10]++
		n = n / 10
	}
	// fmt.Println(arr)
	for k, v := range arr {
		if k != 4 && k != 7 {
			if v > 0 {
				fmt.Println("NO")
				break
			}
		}
	}
	if arr[4]+arr[7] == 4 || arr[4]+arr[7] == 7 {
		fmt.Println("YES")
	}
}

// func main() { cf110a(os.Stdin, os.Stdout) }
