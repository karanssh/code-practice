package main

import (
	"strconv"
	"strings"
)

func rotatedDigits(N int) int {
	count := 0
	for i := 1; i <= N; i++ {
		s := strconv.Itoa(i)
		if strings.Contains(s, "3") || strings.Contains(s, "4") || strings.Contains(s, "7") {
			continue
		} else if strings.Contains(s, "2") || strings.Contains(s, "5") || strings.Contains(s, "6") || strings.Contains(s, "9") {
			count++
			continue
		}
	}
	return count
}
