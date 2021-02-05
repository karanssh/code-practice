package main

import (
	"math"
)

// func main() {
// 	var arr = []int{2, 3, 4, 5}
// 	fmt.Print(maxProduct(arr))
// }
func maxProduct(nums []int) int {
	var posa, posb, nega, negb int
	posa = int(math.Inf(-1))
	posb = int(math.Inf(-1))
	nega = int(math.Inf(-1))
	negb = int(math.Inf(-1))
	if len(nums) == 2 {
		return (nums[0] - 1) * (nums[1] - 1)
	}
	for k, v := range nums {
		if nums[k] > posa {
			posb = posa
			posa = nums[k]
		} else if nums[k] > posb {
			posb = nums[k]
		}

		if v < 0 && int(math.Abs(float64(v))) > int(math.Abs(float64(nega))) {
			negb = nega
			nega = v
		} else if v < 0 && int(math.Abs(float64(v))) > int(math.Abs(float64(negb))) {
			negb = v
		}
	}
	if negb*nega > posa*posb {
		return (negb - 1) * (nega - 1)
	}
	return (posa - 1) * (posb - 1)
}
