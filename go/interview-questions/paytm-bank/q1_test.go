package main

import (
	"testing"
)

func Test_foo(t *testing.T) {
	tests := []struct {
		name string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		testData := []int{5, -4, -1, 2, 3, 9}
		t.Run(tt.name, func(t *testing.T) {
			foo(0, testData)
		})
	}
}

func Test_main(t *testing.T) {
	tests := []struct {
		name string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			main()
		})
	}
}
