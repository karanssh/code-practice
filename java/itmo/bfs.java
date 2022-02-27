package itmo;

import java.util.*;

public class bfs {
    
    public static List<List<Integer>> traverse(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();

        if (root== null ) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();

        queue.add(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>(levelSize);
            for (int i=0; i<levelSize; i++) {
                TreeNode currentNode = queue.poll();
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

    public static List<List<Integer>> zigZagTraverse(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();

        if (root== null ) {
            return result;
        }

        Deque<TreeNode> queue = new ArrayDeque<>();

        queue.addLast(root);
        boolean traverseOrder = false;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            traverseOrder = !traverseOrder;
            List<Integer> currentLevel = new ArrayList<>(levelSize);
            for (int i=0; i<levelSize; i++) {
                TreeNode currentNode = queue.poll();
                currentLevel.add(currentNode.val);

                if (traverseOrder) {
                    if (currentNode.right!= null) {
                        queue.addLast(currentNode.right);
                    }

                    if (currentNode.left!= null) {
                        queue.addLast(currentNode.left);
                    }
                    
                   
                } else {
                    if (currentNode.left!= null) {
                        queue.addLast(currentNode.left);
                    }
                    
                    if (currentNode.right!= null) {
                        queue.addLast(currentNode.right);
                    }
                }

                
                
            }
            result.add(currentLevel);

        }

        return result;
    }

    public static int maxDepth(TreeNode root) {
        int maxDepth = 0;

        if (root== null ) {
            return 0;
        }

        Queue<TreeNode> queue = new LinkedList<>();

        queue.add(root);

        while (!queue.isEmpty()) {

            maxDepth++;
            int levelSize = queue.size();
            for (int i=0; i<levelSize; i++) {
                TreeNode currentNode = queue.poll();

                if (currentNode.left!= null) {
                    queue.add(currentNode.left);
                }
                
                if (currentNode.right!= null) {
                    queue.add(currentNode.right);
                }
                
            }

        }

        return maxDepth;
    }

    public static List<List<Integer>> binaryTreeTraverseLevelOrder2(TreeNode root) {
        List<List<Integer>> result = new LinkedList<>();

        if (root== null ) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();

        queue.add(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>(levelSize);
            for (int i=0; i<levelSize; i++) {
                TreeNode currentNode = queue.poll();
                currentLevel.add(currentNode.val);

                if (currentNode.left!= null) {
                    queue.add(currentNode.left);
                }
                
                if (currentNode.right!= null) {
                    queue.add(currentNode.right);
                }
                
            }
            result.add(0, currentLevel);

        }

        return result;
    }
    public int widthOfBinaryTree(TreeNode root) {
        if(null == root) {
           return 0;
       }
       Map<TreeNode, Integer> mp;
       ArrayDeque<Map<TreeNode, Integer>> queue = new ArrayDeque<>();
       mp = new HashMap<>();
       mp.put(root, 0);
       queue.add(mp);
       int ans = 0;
       while(!queue.isEmpty()) {
           int sz = queue.size();
           Map<TreeNode, Integer> first = queue.getFirst();
           Map<TreeNode, Integer> last = queue.getLast();
           ans = Math.max(ans, (Integer) last.values().toArray()[0] - (Integer) first.values().toArray()[0] + 1);
           Map<TreeNode, Integer> node;
           for (int i = 0; i < sz; i++) {
               node = queue.poll();
               TreeNode n = (TreeNode) node.keySet().toArray()[0];
               Integer value = (Integer) node.values().toArray()[0];
               if (n.left != null) {
                   mp = new HashMap<>();
                   mp.put(n.left, 2 * value + 1);
                   queue.add(mp);
               }
               if (n.right != null) {
                   mp = new HashMap<>();
                   mp.put(n.right, 2 * value + 2);
                   queue.add(mp);
               }
           }
       }
       return ans;
   }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(12);
        root.left = new TreeNode(7);
        root.right = new TreeNode(5);

        List<List<Integer>> res = bfs.traverse(root);
        System.out.println("result is: " + res);
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