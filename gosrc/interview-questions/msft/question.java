import java.util.LinkedList;
import java.util.Queue;

public class question {
    public static void main(String[] args) {
        System.out.println("hello there");

    }

    
    public static void main2(String[] args) {
        TreeNode root = new TreeNode(12);
        root.left = new TreeNode(7);
        root.right = new TreeNode(5);
        root.left.left = new TreeNode(8);
        root.right.left = new TreeNode(9);

        System.out.println("result is: " + question.findSuccessor(root , 9).val);

    }
    public static TreeNode findSuccessor(TreeNode root, int key) {

        boolean retNext = false;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root); 
       
        while (!q.isEmpty()) {

           
            int levelSize = q.size();
            for (int i=0; i<levelSize; i ++) {
            TreeNode curr = q.poll();
            if (curr.val == key) {
                // return something
                TreeNode nextNode = q.poll();
                if (nextNode!= null) {
                    return nextNode;
                } else {
                    retNext = true; 
                }
            }

            if (curr.left!= null) {
                if (retNext) {
                    return curr.left;
                }
                q.add(curr.left);
            }
            
            if (curr.right!= null) {
                if (retNext) {
                    return curr.right;
                }
                q.add(curr.right);
            }
        }

        }

        return null;
    }
}


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
} 