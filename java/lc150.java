import java.util.ArrayDeque;
import java.util.Deque;

public class lc150 {
    public static void main(String[] args) {
        System.out.println(evalRPN(new String[] {"4","3","-"}));
        System.out.println(evalRPN(new String[] {"2","1","+","3","*"}));
        System.out.println(evalRPN(new String[] {"4","13","5","/","+"}));
        System.out.println(evalRPN(new String[] {"10","6","9","3","+","-11","*","/","*","17","+","5","+"}));
    }

    public static int evalRPN(String[] tokens) {
        int ans = 0;
        Deque<String> st = new ArrayDeque<>();

        for (String s : tokens) {
            switch (s) {
                case "+":
                    int op1 = Integer.parseInt(st.pop());
                    int op2 = Integer.parseInt(st.pop());
                    ans = op2 + op1;
                    st.push(ans + "");
                    break;
                case "-":
                    op1 = Integer.parseInt(st.pop());
                    op2 = Integer.parseInt(st.pop());
                    ans = op2 - op1;
                    st.push(ans + "");
                    break;
                case "*":
                    op1 = Integer.parseInt(st.pop());
                    op2 = Integer.parseInt(st.pop());
                    ans = op1 * op2;
                    st.push(ans + "");
                    break;
                case "/":
                    op1 = Integer.parseInt(st.pop());
                    op2 = Integer.parseInt(st.pop());
                    ans = op2 / op1;
                    st.push(ans + "");
                    break;
                default:
                    st.push(s);
            }
        }
        return Integer.parseInt(st.peek());

    }
}
