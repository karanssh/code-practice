package main

import (
	"fmt"
	"io"
	"strings"
)

func cf133A(in io.Reader, out io.Writer) {
	var a string
	fmt.Fscan(in, &a)
	if strings.Contains(a, "H") || strings.Contains(a, "Q") || strings.Contains(a, "9") {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}

// func main() { cf133A(os.Stdin, os.Stdout) }
