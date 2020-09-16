package main

import (
	"fmt"
	"io"
)

func cf977a(in io.Reader, out io.Writer) {
	var k, n int
	fmt.Fscan(in, &k, &n)
	for n != 0 {
		n--
		if k%10 == 0 {
			k = k / 10
		} else {
			k--
		}
	}
	fmt.Println(k)
}

// func main() { cf977a(os.Stdin, os.Stdout) }
