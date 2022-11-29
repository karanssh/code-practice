package main

import (
	"fmt"
	"io"
)

func cf41A(in io.Reader, out io.Writer) {
	var a, b string
	fmt.Fscan(in, &a, &b)
	if reverse(b) == a {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}
func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// func main() { cf41A(os.Stdin, os.Stdout) }
