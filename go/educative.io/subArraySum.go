package main

func findAverageContiguousSubArrays(arr []int, k int) []float64 {
	resultArray := make([]float64, len(arr)-k+1)
	windowStart := 0
	windowSum := 0.0
	for windowEnd := 0; windowEnd < len(arr); windowEnd++ {
		windowSum += float64(arr[windowEnd])
		if windowEnd >= k-1 {
			resultArray[windowStart] = windowSum / float64(k)
			windowSum -= float64(arr[windowStart])
			windowStart++
		}
	}
	return resultArray
}

func findMaxSumContiguousSubArrays(arr []int, k int) int {
	var max int
	max = -222222
	windowStart := 0
	windowSum := 0
	for windowEnd := 0; windowEnd < len(arr); windowEnd++ {
		windowSum += (arr[windowEnd])
		if windowEnd >= k-1 {
			if max <= windowSum {
				max = windowSum
			}
			windowSum -= (arr[windowStart])
			windowStart++
		}
	}
	return max
}
