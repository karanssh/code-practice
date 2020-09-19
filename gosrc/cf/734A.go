package main

import (
	"fmt"
	"io"
	"os"
)

func cf734a(in io.Reader, out io.Writer) {
	var a string
	var n, Awins, Dwins int
	fmt.Fscan(in, &n)
	fmt.Fscan(in, &a)
	runes := []rune(a)
	for i := 0; i < len(runes); i++ {
		if runes[i] == 'A' {
			Awins++
		}
		if runes[i] == 'D' {
			Dwins++
		}
	}
	// fmt.Println(Awins)
	// fmt.Println(Dwins)

	if Awins > Dwins {
		fmt.Println("Anton")
	} else if Awins < Dwins {
		fmt.Println("Danik")
	} else if Awins == Dwins {
		fmt.Println("Friendship")

	}

}

func main() { cf734a(os.Stdin, os.Stdout) }
