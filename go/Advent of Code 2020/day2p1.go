package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func day2p1(in io.Reader, out io.Writer) {
	validPass := 0
	dat, err := readLines("input.txt")
	if err != nil {
		fmt.Println(err)
	}

	//	fmt.Println(dat)
	// arrSize := len(dat)
	for _, v := range dat {
		temp := strings.Split(v, " ")
		rangeOfData := temp[0]
		charCompulsory := temp[1][:1]
		passwordToCheck := temp[2]
		// fmt.Println("range of data :", rangeOfData)
		// fmt.Println("compulsorychar ", charCompulsory)
		// fmt.Println("password:", passwordToCheck)
		numberOfOccurences := strings.Count(passwordToCheck, charCompulsory)
		rangeDataBreakup := strings.Split(rangeOfData, "-")
		lowerBound, _ := strconv.Atoi(rangeDataBreakup[0])
		upperBound, _ := strconv.Atoi(rangeDataBreakup[1])

		if numberOfOccurences >= lowerBound && numberOfOccurences <= upperBound {
			validPass++
		}

		// fmt.Println("occurences ", numberOfOccurences)

		// fmt.Println(temp)
	}
	fmt.Println("number of valid passwords", validPass)
}
func day2p2(in io.Reader, out io.Writer) {
	validPass := 0
	dat, err := readLines("input.txt")
	if err != nil {
		fmt.Println(err)
	}

	//	fmt.Println(dat)
	// arrSize := len(dat)
	for _, v := range dat {
		temp := strings.Split(v, " ")
		rangeOfData := temp[0]
		charCompulsory := temp[1][:1]
		passwordToCheck := temp[2]
		// fmt.Println("range of data :", rangeOfData)
		// fmt.Println("compulsorychar ", charCompulsory)
		// fmt.Println("password:", passwordToCheck)
		// numberOfOccurences := strings.Count(passwordToCheck, charCompulsory)
		rangeDataBreakup := strings.Split(rangeOfData, "-")
		lowerBound, _ := strconv.Atoi(rangeDataBreakup[0])
		upperBound, _ := strconv.Atoi(rangeDataBreakup[1])
		lowerBound = lowerBound - 1
		upperBound = upperBound - 1
		// fmt.Println(string(passwordToCheck[lowerBound]))
		// fmt.Println(string(passwordToCheck[upperBound]))

		if (string(passwordToCheck[lowerBound]) == charCompulsory || string(passwordToCheck[upperBound]) == charCompulsory) &&
			!(string(passwordToCheck[lowerBound]) == charCompulsory && string(passwordToCheck[upperBound]) == charCompulsory) {
			validPass++
		}
		//break
		// fmt.Println("occurences ", numberOfOccurences)

		// fmt.Println(temp)
	}
	fmt.Println("number of valid passwords", validPass)
}

// readLines reads a whole file into memory
// and returns a slice of its ints.
func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func main() {
	// day2p1(os.Stdin, os.Stdout)
	day2p2(os.Stdin, os.Stdout)
}
