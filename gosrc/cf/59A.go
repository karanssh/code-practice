package main

import (
	"fmt"
	"io"
	"os"
	"strings"
	"unicode"
)

func cf59a(in io.Reader, out io.Writer) {
	var n string
	var upperCount, lowerCount int
	fmt.Fscan(in, &n)
	for _, v := range n {
		if unicode.IsUpper(v) {
			upperCount++
		}
		if unicode.IsLower(v) {
			lowerCount++
		}
	}
	if upperCount > lowerCount {
		fmt.Println(strings.ToUpper(n))

	} else {
		fmt.Println(strings.ToLower(n))
	}

}

func main() { cf59a(os.Stdin, os.Stdout) }
