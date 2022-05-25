package main

import "fmt"

var (
	timeValue map[int]map[int]int
)

func main() {
	fmt.Println("say hi")

	set(1, 1, 0)
	set(1, 2, 2)
	fmt.Println(get(1, 2))

	set(1, 5, 2)
	fmt.Println(get(1, 2))

}

func get(key, time int) (int, bool) {
	if timeValue == nil {
		return 0, false
	}
	//map[key]map[time]value
	anotherMap, ok := timeValue[key]
	if !ok {
		return 0, false
	}
	val, found := anotherMap[time]
	if !found {
		// return the value at the most recent timepoint
		max := -9999
		val := 0
		for k, v := range anotherMap {
			if v > max {
				val = v
				max = k
			}
		}
		return val, true
	}
	return val, found
}

func set(key, value, time int) {
	if timeValue == nil {
		timeValue = make(map[int]map[int]int)
	}
	if time < 0 {
		return
	}
	// timeValue[key] = map[int]int{
	// 	time: value,
	// }

	_, ok := timeValue[key]
	if ok {
		// append
		timeValue[key][time] = value
		return
	}
	timeValue[key] = map[int]int{
		time: value,
	}
}
