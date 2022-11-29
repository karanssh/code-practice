package main

// func main() {
// 	fmt.Println(shuffle([]int{2, 5, 1, 3, 4, 7}, 3))
// 	fmt.Println(shuffle([]int{1, 2, 3, 4, 4, 3, 2, 1}, 4))
// 	fmt.Println(shuffle([]int{1, 1, 2, 2}, 2))

// }

func shuffle(nums []int, n int) []int {
	newArr := make([]int, 0)
	temp := n
	for i := 0; i <= n-1; i++ {
		newArr = append(newArr, nums[i])
		newArr = append(newArr, nums[temp])
		temp++
	}
	return newArr
}
