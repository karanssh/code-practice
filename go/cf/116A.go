package main

import (
	"fmt"
	"io"
)

func cf116A(in io.Reader, out io.Writer) {
	var n, capacity, occupancy int
	capacity = 0
	occupancy = 0
	fmt.Fscan(in, &n)
	// fmt.Print(k, n, w)
	for n != 0 {
		n--
		var inbound, outbound int
		fmt.Fscan(in, &outbound, &inbound)
		occupancy = occupancy + inbound - outbound
		if occupancy > capacity {
			capacity = occupancy
		}

	}

	fmt.Println(capacity)

}

// func main() { cf116A(os.Stdin, os.Stdout) }
