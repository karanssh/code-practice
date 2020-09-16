package main

import (
	"fmt"
	"io"
)

func cf791A(in io.Reader, out io.Writer) {
	var a, b, sum int
	sum = 0
	fmt.Fscan(in, &a, &b)
	// fmt.Print(k, n, w)
	if a <= 0 || b <= 0 {
		return
	}
	for a <= b {
		sum++
		a = a * 3
		b = b * 2

	}
	fmt.Println(sum)

}

// func main() { cf791A(os.Stdin, os.Stdout) }
