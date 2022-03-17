import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

public class lc856 {
    public int scoreOfParentheses(String s) {

        Stack<Integer> stack = new Stack<Integer>();
        int cur = 0;
        for(char c : s.toCharArray()){
            if(c == '('){
                stack.push(cur);
                cur = 0;
            } else {
                cur = stack.pop() + Math.max(1, cur*2);
            }
        }
        return cur;
    }

    public static void main(String[] args) {
      

        lc856 obj = new lc856();

        System.out.println(obj.scoreOfParentheses("()"));
        System.out.println(obj.scoreOfParentheses("(())"));
        System.out.println(obj.scoreOfParentheses("()()"));

        


    }
}
