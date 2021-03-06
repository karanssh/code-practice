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
