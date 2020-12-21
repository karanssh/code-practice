package main

import "fmt"

func generateMatrix(n int) [][]int {
	matrix := make([][]int, n)
	for i := range matrix {
		matrix[i] = make([]int, n)
	}
	if n == 0 {
		return matrix
	}
	rowBegin := 0
	rowEnd := n - 1
	colBegin := 0
	colEnd := n - 1

	initNum := 1
	var i int
	for rowBegin <= rowEnd && colBegin <= colEnd {
		//left --> right
		for i = colBegin; i <= colEnd; i++ {

			matrix[rowBegin][i] = initNum
			initNum++
		}
		rowBegin++

		//up --> down
		for i := rowBegin; i <= rowEnd; i++ {

			matrix[i][colEnd] = initNum
			initNum++
		}
		colEnd--

		//right --> left;
		for i := colEnd; i >= colBegin; i-- {

			matrix[rowEnd][i] = initNum
			initNum++
		}
		rowEnd--

		//down --> up
		for i := rowEnd; i >= rowBegin; i-- {

			matrix[i][colBegin] = initNum
			initNum++
		}
		colBegin++

	}
	return matrix
}
func main() {
	temp := generateMatrix(3)
	fmt.Println(temp)
}
