package main

import (
	"reflect"
	"testing"
)

func Test_findAverageContiguousSubArrays(t *testing.T) {
	type args struct {
		arr []int
		k   int
	}
	tests := []struct {
		name string
		args args
		want []float64
	}{
		{
			name: "karan1",
			args: args{
				arr: []int{1, 2, 3, 4, 5, 6, 7, 8},
				k:   3,
			},
			want: []float64{2, 3, 4, 5, 6, 7},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findAverageContiguousSubArrays(tt.args.arr, tt.args.k); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("findAverageContiguousSubArrays() = %v, want %v", got, tt.want)
			}
		})
	}
}
