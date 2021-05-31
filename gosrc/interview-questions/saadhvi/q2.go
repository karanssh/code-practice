package main

import "fmt"

/*
Implement the function fillChannel so that:

It creates a channel of integers with a size that is the same as the number of functions received.
Functions received as an argument should be executed in parallel.
As soon as a function finishes, its result should be written to the channel.
fillChannel should return the channel immediately, without waiting for functions to end.
For example, executing main function should produce the following console output:

Result: 10000000
Result: 200000000
*/

func fillChannel(functions ...func() int) chan int {
	resultChan := make(chan int, len(functions))
	for _, v := range functions {
		go func(v func() int) {
			resultChan <- v()
		}(v)

	}
	return resultChan
}

func exampleFunction(counter int) int {
	sum := 0
	for i := 0; i < counter; i++ {
		sum += 1
	}
	return sum
}

func main() {
	sizeOfFunc := 4

	ch1 := fillChannel(func() int { return exampleFunction(20) }, func() int { return exampleFunction(30) }, func() int { return exampleFunction(40) }, func() int { return exampleFunction(50) })

	for count := 0; count < sizeOfFunc; count++ {
		fmt.Println(<-ch1)
	}
	return
}
