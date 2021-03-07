package main

import "testing"

func Test_longestSubstringKDistinct(t *testing.T) {
	type args struct {
		str string
		k   int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{
			name: "test 1",
			args: args{
				str: "araaci",
				k:   2,
			},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestSubstringKDistinct(tt.args.str, tt.args.k); got != tt.want {
				t.Errorf("longestSubstringKDistinct() = %v, want %v", got, tt.want)
			}
		})
	}
}
