package main

import (
	"fmt"
	"io"
)

func cf617a(in io.Reader, out io.Writer) {
	var n, steps int
	fmt.Fscan(in, &n)
	for n != 0 {
		if n >= 5 {
			steps = steps + n/5
			n = n % 5
		}
		if n >= 4 {
			steps = steps + n/4
			n = n % 4
		}
		if n >= 3 {
			steps = steps + n/3
			n = n % 3
		}
		if n >= 2 {
			steps = steps + n/2
			n = n % 2
		}
		if n >= 1 {
			steps = steps + n/1
			n = n % 1
		}
	}

	fmt.Println(steps)
}

// func main() { cf617a(os.Stdin, os.Stdout) }
