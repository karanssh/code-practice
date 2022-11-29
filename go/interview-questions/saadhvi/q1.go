package main

import "fmt"

/*
Implement the findAllHobbyists function that takes a hobby, and a map consisting of people's names mapped to their respective hobbies. The function should return a

slice containing the names of the people (in any order) who enjoy the hobby.

For example, the following code should display the name 'Chad'.

hobbies := map[string][]string {
    "Steve": []string{"Fashion", "Piano", "Reading"},
    "Patty": []string{"Drama", "Magic", "Pets"},
    "Chad": []string{"Puzzles", "Pets", "Yoga"},
}
*/
// Main function
func main() {
	hobbies := map[string][]string{
		"Steve": []string{"Fashion", "Piano", "Reading"},
		"Patty": []string{"Drama", "Magic", "Pets"},
		"Chad":  []string{"Puzzles", "Pets", "Yoga"},
	}
	fmt.Println(findAllHobbyists(hobbies, "Piano"))
	fmt.Println(findAllHobbyists(hobbies, "Yoga"))

}

func findAllHobbyists(inputMap map[string][]string, hobbyName string) []string {
	outputMap := make([]string, 0)
	for k, v := range inputMap {
		for _, v1 := range v {
			if v1 == hobbyName {
				outputMap = append(outputMap, k)
			}
		}
	}
	return outputMap
}
