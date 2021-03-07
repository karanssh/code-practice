package main

func longestSubstringKDistinct(str string, k int) int {
	windowStart := 0
	maxLength := 0
	charFreqMap := make(map[string]int)
	for windowEnd := 0; windowEnd < len(str); windowEnd++ {
		rightChar := string(str[windowEnd])
		charFreqMap[rightChar] = charFreqMap[rightChar] + 1
		for len(charFreqMap) > k {
			leftChar := string(str[windowStart])
			charFreqMap[leftChar] = charFreqMap[leftChar] - 1
			if charFreqMap[leftChar] == 0 {
				delete(charFreqMap, leftChar)
			}
			windowStart++
		}
		maxLength = max(maxLength, windowEnd-windowStart+1)

	}
	return maxLength
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
