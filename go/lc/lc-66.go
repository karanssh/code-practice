package main

func plusOne(digits []int) []int {
	newArr := make([]int, len(digits))
	addNeed := true
	for i := len(digits) - 1; i >= 0; i-- {
		if addNeed {
			if digits[i] == 9 {
				addNeed = true
				newArr[i] = 0
				if i == 0 && digits[i] == 9 {
					newArr = append([]int{1}, newArr...)
				}
			} else {
				if i == 0 && digits[i] == 9 {
					newArr = append([]int{1}, newArr...)

				} else {
					newArr[i] = digits[i] + 1

				}
				addNeed = false
			}
		} else {
			newArr[i] = digits[i]
		}

	}
	return newArr

}

// func main() {
// 	fmt.Println(
// 		plusOne([]int{0}),
// 		plusOne([]int{4, 3, 2, 9}),
// 		plusOne([]int{4, 3, 9, 9}),
// 		plusOne([]int{9, 9, 9, 9}),
// 	)

// }
