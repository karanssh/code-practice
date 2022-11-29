package main

import (
	"fmt"
	"io"
)

func cf467a(in io.Reader, out io.Writer) {

	var n, occupied, total, eligible int
	fmt.Fscan(in, &n)
	for n > 0 {
		n--
		fmt.Fscan(in, &occupied, &total)
		if total-occupied >= 2 {
			eligible++
		}
	}
	fmt.Println(eligible)
}

// func main() { cf467a(os.Stdin, os.Stdout) }
