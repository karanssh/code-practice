package main

type (
	Stack struct {
		top    *node
		lenght int
	}
	node struct {
		value interface{}
		prev  *node
	}
)

func New() *Stack {
	return &Stack{nil, 0}
}

func (s *Stack) Len() int {
	return s.lenght
}

func (s *Stack) Peek() interface{} {
	if s == nil {
		return nil
	}
	return s.top.value
}
func (s *Stack) Push(value interface{}) {
	n := &node{value, s.top}
	s.top = n
	s.lenght++
}

func (s *Stack) Pop() interface{} {
	if s.lenght == 0 {
		return nil
	}
	n := s.top
	s.top = n.prev
	s.lenght--
	return n.value
}
