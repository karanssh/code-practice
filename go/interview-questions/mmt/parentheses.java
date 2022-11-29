import java.util.Stack;

class parentheses {
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
    public static void main(String[] args) {
        System.out.println(isValid("[]"));
        System.out.println(isValid("[{}]"));
        System.out.println(isValid("[}(){]"));
        System.out.println(isValid("[{(})]"));

        /*
        [{}]		true
[{()}]		true
[{()]		false
[{(})]		false	
[}(){]		false
        */
    }
}