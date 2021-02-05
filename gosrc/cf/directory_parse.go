package main

import (
	"fmt"
	pathUtil "path"
	"strings"
)

//leet code feb 6 challenge

type (
	//Stack data structure
	Stack struct {
		top    *node
		length int
	}
	node struct {
		value interface{}
		prev  *node
	}
)

//NewStack Create a new stack
func NewStack() *Stack {
	return &Stack{nil, 0}
}

//Len Return the number of items in the stack
func (s *Stack) Len() int {
	return s.length
}

//Peek View the top item on the stack
func (s *Stack) Peek() interface{} {
	if s.length == 0 {
		return nil
	}
	return s.top.value
}

// Pop the top item of the stack and return it
func (s *Stack) Pop() interface{} {
	if s.length == 0 {
		return nil
	}

	n := s.top
	s.top = n.prev
	s.length--
	return n.value
}

// Push a value onto the top of the stack
func (s *Stack) Push(value interface{}) {
	n := &node{value, s.top}
	s.top = n
	s.length++
}

func parseDirectory(path string) string {
	charArrPath := []rune(path)
	dirState := NewStack()
	result := "/"

	//get the path length first
	pathLen := len(path)
	for i := 0; i < pathLen; i++ {
		dir := ""
		for i < pathLen && charArrPath[i] == '/' {
			i++
		}
		for i < pathLen && charArrPath[i] != '/' {

			dir += string(charArrPath[i])
			i++
		}
		if dir == ".." {
			if dirState.Peek() != nil {
				_ = dirState.Pop()
			}
		} else if dir == "." {
			continue
		} else if len(dir) != 0 {
			dirState.Push(dir)

		}
	}
	fmt.Println(dirState)
	tempStack := NewStack()
	for dirState.Peek() != nil {
		tempStack.Push(dirState.Pop())
	}
	for tempStack.Peek() != nil {
		if tempStack.length != 1 {
			result += tempStack.Pop().(string) + "/"
		} else {
			result += tempStack.Pop().(string)
		}
	}
	newRes := strings.Split(result, "/")
	result = "/" + newRes[len(newRes)-1]
	return result
}
func imp1(path string) string {
	pathList := []string{}

	parsePath := func(path string) {
		if path == ".." {
			if len(pathList) > 0 {
				pathList = pathList[:len(pathList)-1]
			}
		} else if path == "." {
		} else {
			pathList = append(pathList, path)
		}
	}

	startIndex := 0
	i := 1
	for ; i < len(path) && path[i] == '/'; i++ {
	}
	startIndex = i
	for ; i < len(path); i++ {
		if path[i] == '/' {

			subPath := path[startIndex:i]
			parsePath(subPath)

			for ; i < len(path) && path[i] == '/'; i++ {
			}

			startIndex = i
		}
	}

	if startIndex < len(path) {
		parsePath(path[startIndex:])
	}

	result := "/"
	for i := 0; i < len(pathList); i++ {
		result += pathList[i]
		if i != len(pathList)-1 {
			result += "/"
		}
	}

	return result
}
func simplifyPath(path string) string {
	return pathUtil.Clean(path)
}
func main() {
	fmt.Println(parseDirectory("/a/./b/../../c/"))

}
