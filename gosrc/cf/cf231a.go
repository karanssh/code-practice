package main

import (
	"fmt"
	"io"
	"os"
)

func cf231a(in io.Reader, out io.Writer) {
	var n int
	var a, b, c int
	var total int
	fmt.Fscan(in, &n)
	for n > 0 {
		n--
		fmt.Fscan(in, &a, &b, &c)
		if (a == 1 && b == 1) || (c == 1 && b == 1) || (a == 1 && c == 1) {
			total++
		}

	}

	fmt.Println(total)

}

func main() { cf231a(os.Stdin, os.Stdout) }
