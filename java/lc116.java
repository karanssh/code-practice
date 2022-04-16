import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class lc116 {
    public static Node connect(Node root) {
       

        if (root== null ) {
            return root;
        }

        Queue<Node> queue = new LinkedList<>();

        queue.add(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            	Node preNode = null;
            for (int i=0; i<levelSize; i++) {
                Node currentNode = queue.poll();
                
                if (preNode != null) {
					preNode.next = currentNode;
				}
				preNode = currentNode;
                

                if (currentNode.left!= null) {
                    queue.add(currentNode.left);
                }
                
                if (currentNode.right!= null) {
                    queue.add(currentNode.right);
                }
                
            }
            

        }

        return root;
    }
    public static void main(String[] args) {
        Node root = new Node();
        root.val = 1;
        //Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);

        Node temp = connect(root);
        System.out.println(traverse(temp));


    }
    public static List<List<Integer>> traverse(Node root) {
        List<List<Integer>> result = new ArrayList<>();

        if (root== null ) {
            return result;
        }

        Queue<Node> queue = new LinkedList<>();

        queue.add(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>(levelSize);
            for (int i=0; i<levelSize; i++) {
                Node currentNode = queue.poll();
                currentLevel.add(currentNode.val);

                if (currentNode.left!= null) {
                    queue.add(currentNode.left);
                }
                
                if (currentNode.right!= null) {
                    queue.add(currentNode.right);
                }
                
            }
            result.add(currentLevel);

        }

        return result;
    }

}


// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};


class Solution {
    public Node connect(Node root) {
       

        if (root== null ) {
            return root;
        }

        Queue<Node> queue = new LinkedList<>();

        queue.add(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>(levelSize);
            for (int i=0; i<levelSize; i++) {
                Node currentNode = queue.poll();
                currentNode.next = queue.peek();
                currentLevel.add(currentNode.val);

                if (currentNode.left!= null) {
                    queue.add(currentNode.left);
                }
                
                if (currentNode.right!= null) {
                    queue.add(currentNode.right);
                }
                
            }
            

        }

        return root;
    }
}