package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
)

func day1p2(in io.Reader, out io.Writer) {
	targetVal := 2020
	dat, err := readLines("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	sort.Ints(dat)
	fmt.Println(dat)
	arrSize := len(dat)
	for i := 0; i < arrSize-2; i++ {

		left := i + 1
		right := arrSize - 1
		for left < right {
			if dat[i]+dat[left]+dat[right] == targetVal {
				fmt.Println("Triplet is ", dat[i], ", ", dat[left], ", ", dat[right])
				fmt.Println("Product is ", dat[i]*dat[left]*dat[right])
				return
			} else if dat[i]+dat[left]+dat[right] < targetVal {
				left++
			} else {
				right--
			}
		}
	}

}

// readLines reads a whole file into memory
// and returns a slice of its ints.
func readLines(path string) ([]int, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		intVal, _ := strconv.Atoi(scanner.Text())
		lines = append(lines, intVal)
	}
	return lines, scanner.Err()
}

func main() { day1p2(os.Stdin, os.Stdout) }
