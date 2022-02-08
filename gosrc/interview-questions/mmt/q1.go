package main

import (
	"fmt"
)

/*


 */

func main() {
	fmt.Println(foo("{]"))
	fmt.Println(foo("[{()}]"))

	fmt.Println(foo("[}(){]"))

	fmt.Println(foo("{]"))

}

func foo(s string) bool {
	//fmt.Print("hello")
	var st Stack
	st.lenght = 0
	st.top = nil

	for _, c := range s {
		if c == '(' {
			st.Push(')')
		} else if c == '{' {
			st.Push('}')
		} else if c == '[' {
			st.Push(']')
		} else if st.lenght == 0 || st.Pop() != c {
			return false
		}
	}
	if st.lenght == 0 {
		return true
	}
	return false

	/*
			 public static boolean isValid(String s) {
		        Stack<Character> st = new Stack<Character>();
		        for (char c : s.toCharArray()) {
		            if (c=='(') {
		                st.push(')');
		            } else if (c=='{') {
		                st.push('}');
		            } else if (c=='[') {
		                st.push(']');
		            } else if (st.isEmpty() || st.pop() != c) {
		                return false;
		            }
		        }
		        return st.isEmpty();
		    }
	*/
}

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
