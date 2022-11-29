package main

import (
	"fmt"
	"reflect"
	"sort"
)

func main() {
	//lol I panic wrote this in 4 fucking minutes I know it sucks whatever idgaf
	s := "anagram"
	t := "nagaram"

	sArr := make([]string, 0)
	tArr := make([]string, 0)

	for _, v := range s {
		sArr = append(sArr, string(v))
	}
	for _, v := range t {
		tArr = append(tArr, string(v))
	}

	sort.Strings(sArr)
	sort.Strings(tArr)

	if !reflect.DeepEqual(sArr, tArr) {
		fmt.Println("not an anagram")
	} else {
		fmt.Println("anagram")
	}

}
