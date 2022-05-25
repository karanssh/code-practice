package main

import (
	"testing"
)

func Test_main(t *testing.T) {
	tests := []struct {
		name string
	}{
		{
			name: "test hi",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			main()
		})
	}
}

func Test_get(t *testing.T) {
	type args struct {
		key  int
		time int
	}
	timeValue = map[int]map[int]int{
		1: map[int]int{
			0: 1,
			2: 2,
		},
	}
	tests := []struct {
		name  string
		args  args
		want  int
		want1 bool
	}{
		{
			name: "get 1, 1",
			args: args{
				key:  1,
				time: 0,
			},
			want:  1,
			want1: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := get(tt.args.key, tt.args.time)
			if got != tt.want {
				t.Errorf("get() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("get() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func Test_set(t *testing.T) {
	type args struct {
		key   int
		value int
		time  int
	}
	tests := []struct {
		name string
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			set(tt.args.key, tt.args.value, tt.args.time)
		})
	}
}
