package main

func twoSum(numbers []int, target int) []int {
	t := make(map[int]int)
	for i, n := range numbers {
		if i0, ok := t[target-n]; ok {
			return []int{i0 + 1, i + 1}
		}
		t[n] = i
	}
	return []int{1, len(numbers)}
}

func twoSumV2(numbers []int, target int) []int {
	left := 0
	right := len(numbers) - 1
	for left < right {
		currentSum := numbers[left] + numbers[right]
		if currentSum == target {
			return []int{left + 1, right + 1}
		} else if currentSum < target {
			left++

		} else if currentSum > target {
			right--
		}
	}
	return []int{}

}
