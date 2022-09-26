package main

import "fmt"

func main() {
	var input [][]int
	input = append(input, []int{1, 4})
	input = append(input, []int{2, 6})
	input = append(input, []int{7, 9})
	fmt.Println(findMergedIntervals(input))
	fmt.Println("This is a debug message")
}

type pairValues struct {
	valueA int
	valueB int
}

func findMergedIntervals(arr [][]int) []pairValues {
	start := arr[0][0]
	end := arr[0][1]

	res := make([]pairValues, 0)
	newInterval := pairValues
	for _, v := range arr {

		if v[0] <= end {
			if end > v[1] {
				newInterval = end
			} else {
				newInterval = v[1]
			}
		} else {
			res = append(res, pairValues{valueA: start, valueB: end})
		}

		if end >= v[1] {
			start = v[0]
			end = v[1]
			res = append(res, pairValues{valueA: start, valueB: end})
		} else {

			end = v[1]
			newInterval = interval
		}
	}
	res = append(res, pairValues{valueA: start, valueB: end})
	return res
}

/*
 newInterval

 if interval[0] <= intervals[1] {
	 newInterval = max (newInterva;[1], interval[1])

 } else {
	 res = append(res, interval)
	 newInterval = interval
 }
*/

/*
public List<List<Integer>> findMergedIntervals(int arr[][]) {
        List<List<Integer>> res;
                Arrays.sort(arr, (a,b)->a[0]-b[0]);
                int start = arr[0][0];
                int end = arr[0][1];

                for (int innerVal[] : arr ){

                    if (end>innerVal[1]) {
                        end = innerVal[1];
                    }else {

                      //  res.add(start, end)
                        start = innerVal[0];
                        end = innerVal[1];

                    }
                }
                //res.add(start, end);
                return res;

    }
*/
