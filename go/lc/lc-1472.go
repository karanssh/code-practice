package main

type BrowserHistory struct {
	root *Node
}

type Node struct {
	val  string
	next *Node
	prev *Node
}

func Constructor(homepage string) BrowserHistory {
	return BrowserHistory{
		root: &Node{
			val: homepage,
		},
	}
}

func (this *BrowserHistory) Visit(url string) {
	node := Node{
		val: url,
	}
	node.prev = this.root
	this.root.next = &node
	this.root = this.root.next
}

func (this *BrowserHistory) Back(steps int) string {

	for steps > 0 && this.root.prev != nil {
		this.root = this.root.prev
		steps -= 1
	}
	return this.root.val
}

func (b *BrowserHistory) Forward(steps int) string {
	for steps > 0 && b.root.next != nil {
		b.root = b.root.next
		steps -= 1
	}
	return b.root.val
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * obj := Constructor(homepage);
 * obj.Visit(url);
 * param_2 := obj.Back(steps);
 * param_3 := obj.Forward(steps);
 */
