package main

import (
	"fmt"
	"io"
)

func cf46A(in io.Reader, out io.Writer) {
	var k, n, w, sum int
	fmt.Fscan(in, &k, &n, &w)
	// fmt.Print(k, n, w)
	for i := 1; i <= w; i++ {
		sum = sum + (i * k)
	}
	if sum <= n {
		fmt.Println("0")
	} else {
		fmt.Println(sum - n)
	}

}

// func main() { cf46A(os.Stdin, os.Stdout) }
