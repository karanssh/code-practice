package main

import (
	"fmt"
	"sync"
)

/*
Write a program to compute Multiplication tables 1 .. 1000. Computed in parallel.

*/

func main() {
	foo()
}

func foo() {
	wg := sync.WaitGroup{}

	storeArray := make([][]int, 1000)

	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func(j int) {
			defer wg.Done()
			storeArray[j] = make([]int, 10)
		}(i)
	}
	wg.Wait()
	storeArrayValue := make([]int, 10)
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func(j int, storeArrayValue []int) {
			defer wg.Done()
			storeArrayValueTmp := make([]int, 10)
			for k := 0; k < 10; k++ {
				tmpVal := j * k
				storeArrayValueTmp[k] = tmpVal
			}
			storeArrayValue = storeArrayValueTmp

		}(i, storeArrayValue)
		wg.Wait()
		storeArray[i] = storeArrayValue
	}
	fmt.Println(storeArray)
}
